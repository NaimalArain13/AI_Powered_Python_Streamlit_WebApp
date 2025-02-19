# 🚀 Growth Mindset Goal Setter

A Streamlit-powered web application that helps users set and track their personal growth goals with AI-powered suggestions and motivation.

## 📝 Description

The Growth Mindset Goal Setter is an interactive web application that combines the power of AI with goal-setting best practices. Users can input their 30-day goals and receive personalized AI-generated:
- Goal refinements
- 30-day challenges
- Motivational quotes

The app also includes a built-in progress tracker that helps users monitor their journey over the 30-day period.

## 🛠️ Technologies Used

- Python 3.x
- Streamlit
- Hugging Face API
- python-dotenv

## ⚙️ Installation

1. Clone the repository: 
```bash
git clone <repository-url>
```

2. Install the required dependencies:
```bash
pip install streamlit requests python-dotenv
```

3. Create a `.env` file in the root directory with your Hugging Face API credentials:
```
HUGGINGFACE_API_URL=your_api_url
HUGGINGFACE_API_KEY=your_api_key
```

## 🚀 Usage

1. Run the Streamlit application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the local URL provided by Streamlit (typically http://localhost:8501)

3. Use the application:
   - Enter your goal in the text area
   - Click "Get AI-Powered Advice" to receive personalized suggestions
   - Track your progress using the interactive checkboxes
   - Monitor your completion percentage through the progress bar

## 🎯 Features

- **AI-Powered Goal Refinement**: Receives intelligent suggestions to improve goal clarity and achievability
- **Personalized 30-Day Challenge**: Gets custom-tailored challenges based on your goal
- **Daily Motivation**: Provides AI-generated motivational quotes
- **Progress Tracking**:
  - Weekly organized checkboxes
  - Visual progress bar
  - Completion percentage
  - Progress persistence within session

## 🔒 Environment Variables

The application requires the following environment variables:

- `HUGGINGFACE_API_URL`: Your Hugging Face API endpoint
- `HUGGINGFACE_API_KEY`: Your Hugging Face API authentication key



