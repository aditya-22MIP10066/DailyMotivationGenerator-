
# Daily Motivation Generator

## 🌟 Project Overview

The **Daily Motivation Generator** is a web application designed to provide users with personalized, uplifting motivational messages based on their current mood or situation. Powered by **Google Gemini (Generative AI)**, this tool delivers quick bursts of encouragement, helping users refocus or find inspiration throughout their day.

---

## 🎥 Demo Video

[![Watch the Demo](https://tse2.mm.bing.net/th?id=OIP.FWeWQ5mjNacXwSiKPWK83QHaEK&pid=Api&P=0&h=180)](https://drive.google.com/file/d/1gofdeX0aEJK3phENO1g148VJNQaAwscN/view?usp=sharing)

> 📽️ *Click the image above to watch the demo video.*

---

## ✨ Features

- **🧠 Mood-Based Motivation**  
  Choose from predefined moods or situations (e.g., "Feeling Anxious," "Need Focus," "Feeling Down") to receive a tailored motivational message.

- **🤖 Generative AI Powered**  
  Leverages the Google Gemini API to generate context-aware, unique motivational content.

- **🖥️ Simple Web Interface**  
  Built using HTML, CSS, and JavaScript for a clean, intuitive user experience.

- **🐍 Python Flask Backend**  
  Lightweight backend using Flask to handle API requests and serve content.

- **🔐 Secure API Key Handling**  
  Uses `.env` and `python-dotenv` for environment-based API key management.

---

## 💻 Technologies Used

- **Backend**: Python 3.x, Flask  
- **Frontend**: HTML5, CSS3, JavaScript  
- **AI/NLP**: Google Gemini API (`google-generativeai` Python library)  
- **Dependency Management**: `pip`, `requirements.txt`  
- **Environment Variables**: `python-dotenv`

---

## ⚙️ Setup and Installation

Follow these steps to get the project running locally:

```bash
# clone the repository
git clone [https://github.com/your_username/Daily-Motivation-Generator.git](https://github.com/RupeshSoni665/Motivation_Generator)
cd Daily-Motivation-Generator

# Create virtual environment
python -m venv myvenv

# Activate
# Windows:
myvenv\Scripts\activate

# macOS/Linux:
source myvenv/bin/activate

# install requirements(packages required: flask, python-dortenv and google-generativeai)
pip install -r requirements.txt
```

---

## Obtain Google Gemini API Key

- Visit Google AI Studio.
- Sign in and accept terms.
- Generate a new API key under API settings.
- Copy the API key.

--- 

## Configure Environment Variables

```bash
# Create a .env file in the root directory:
GEMINI_API_KEY="YOUR_FULL_GEMINI_API_KEY_HERE"
```
 
---

## 🚀 Usage

- Open the web app.

- Choose a mood/situation (e.g., "Need Focus").

- Click "Generate Motivation".

- Receive an AI-generated motivational message instantly!

---

## 📁 Project Structure

```bash
gen/
├── app.py                   # Flask backend
├── .env                     # API Key (ignored by Git)
├── requirements.txt         # Dependencies
├── templates/
│   └── index.html           # Main HTML file
└── static/
    ├── css/
    │   └── style.css        # Stylesheet
    └── js/
        └── script.js        # JavaScript logic
```

---


## 🌱 Future Enhancements

- 🔧 Fine-Tuned AI Models: Tailored for motivational tone, productivity, or mental wellness.

- 🎤 Voice Input & Sentiment Detection: More natural input methods.

- 🌈 User Preferences: Save favorite quotes, choose tone (humorous, philosophical, etc.).

- 📈 Feedback System: Rate messages to improve future outputs.

- 📱 Mobile & Desktop Apps: Expand beyond the browser.
