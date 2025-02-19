import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Securely access API credentials
API_URL = os.getenv("HUGGINGFACE_API_URL")
API_KEY = os.getenv("HUGGINGFACE_API_KEY")
HEADERS = {"Authorization": f"Bearer {API_KEY}"}

# Function to get AI response
def get_ai_response(prompt):
    response = requests.post(API_URL, headers=HEADERS, json={"inputs": prompt})
    if response.status_code == 200:
        return response.json()[0]["generated_text"]
    else:
        return "Error: Unable to generate a response. Try again later."

# Streamlit UI
st.title("🚀 Growth Mindset Goal Setter")
st.write("Set your next month's goal & get AI-powered motivation! 💡")

# User Input - Goal
goal = st.text_area("🎯 What's your goal for the next 30 days?", "")

if st.button("Get AI-Powered Advice"):
    with st.spinner("Generating your personalized challenge..."):
        ai_suggestion = get_ai_response(f"Refine this goal: {goal}")
        print(f"AI suggestion {ai_suggestion}")
        challenge = get_ai_response(f"Suggest a 30-day challenge for: {goal}")
        print(f"AI Challenge {challenge}")
        motivation = get_ai_response("Give me a short motivation quote for success")
        print(f"AI motivation {motivation}")
        # Display AI Advice
        st.subheader("📝 Refined Goal Suggestion")
        st.write(ai_suggestion)

        st.subheader("🔥 Personalized Challenge")
        st.write(challenge)

        st.subheader("💡 Daily Motivation")
        st.write(f"{motivation}")


# **✅ Improved Progress Tracker**
st.subheader("📅 Your Progress Tracker")

# Store progress in session state
if "progress" not in st.session_state:
    st.session_state.progress = [False] * 30

# Group days into weeks
week_labels = ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5"]
weeks = [st.session_state.progress[i:i+7] for i in range(0, 30, 7)]

completed_tasks = sum(st.session_state.progress)
progress_percentage = int((completed_tasks / 30) * 100)

# Show Progress Bar
st.progress(progress_percentage / 100)
st.write(f"**🔥 You’ve completed {progress_percentage}% of your challenge! Keep going! 💪**")

# Display checkboxes for each week
for i, week in enumerate(weeks):
    st.subheader(f"{week_labels[i]}")
    for j in range(len(week)):
        st.session_state.progress[i * 7 + j] = st.checkbox(f"Day {i * 7 + j + 1}", value=week[j])

print(st.session_state.progress)      
