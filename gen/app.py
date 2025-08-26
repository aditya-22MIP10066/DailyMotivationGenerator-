import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import google.generativeai as genai

# loading environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Retrieving the API key from environment variables.
API_KEY = os.getenv("GEMINI_API_KEY")

# Raising an error if the API key is not found, indicating a setup issue.
if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables.")

# Configuring the google-generativeai library with API key.
genai.configure(api_key=API_KEY)


# Initializing the Gemini mode, env for generateContent with v1beta.
# changing to 'gemini-2.0-flash' which is often more broadly available and designed for quick text generation tasks.
model = genai.GenerativeModel('gemini-2.0-flash')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_motivation', methods=['POST'])
def generate_motivation():
    """
    Handles the POST request from the frontend to generate a motivational message, expects a JSON payload with a 'mood' field.
    """
    try:
        # Getting the JSON data from the frontend.
        data = request.get_json()
        # Extracting the 'mood' or 'situation' selected.
        moodOrSituation = data.get('mood')

        # Validating if the mood was provided.
        if not moodOrSituation:
            return jsonify({"error": "Mood or situation not provided."}), 400

        # Crafting the instruction for the AI based on input.
        prompt_template = ""
        if moodOrSituation == "Feeling Anxious":
            prompt_template = "Generate a short, encouraging quote or piece of motivation for someone feeling anxious. Focus on themes of calm, presence, and taking things one step at a time. Keep it concise, around 1-2 sentences. Do not use quotation marks around the message. Start directly with the message."
        elif moodOrSituation == "Need Focus":
            prompt_template = "Provide a motivating message for someone who needs focus. Emphasize clarity, productivity, and eliminating distractions. Make it actionable and inspiring. Keep it concise, around 1-2 sentences. Do not use quotation marks around the message. Start directly with the message."
        elif moodOrSituation == "Feeling Down":
            prompt_template = "Offer a brief, uplifting message for someone feeling down. Focus on hope, resilience, and brighter days. Keep it concise, around 1-2 sentences. Do not use quotation marks around the message. Start directly with the message."
        elif moodOrSituation == "Seeking Inspiration":
            prompt_template = "Give a concise inspirational message to spark creativity and new ideas. Keep it around 1-2 sentences. Do not use quotation marks around the message. Start directly with the message."
        elif moodOrSituation == "Overwhelmed":
            prompt_template = "Provide a short, calming message for someone feeling overwhelmed. Focus on breaking tasks down and finding peace. Keep it concise, around 1-2 sentences. Do not use quotation marks around the message. Start directly with the message."
        elif moodOrSituation == "Starting New Project":
            prompt_template = "Generate a brief, encouraging message for someone starting a new project. Focus on excitement, perseverance, and initial steps. Keep it concise, around 1-2 sentences. Do not use quotation marks around the message. Start directly with the message."
        else:
            # Fallback / backup prompt for any other input.
            prompt_template = f"Generate a short, encouraging quote or piece of motivation relevant to '{moodOrSituation}'. Keep it concise, around 1-2 sentences. Do not use quotation marks around the message. Start directly with the message."

        # Sending the prompt to the Gemini model and get the res.
        res = model.generate_content(prompt_template)
        # Extracting the generated text from the model's response.
        motivation_text = res.text

        # Return the generated motivation as a JSON res.
        return jsonify({"motivation": motivation_text})

    except Exception as e:
        # printing the exact exception message to the Flask console,
        print(f"Error generating content: {e}")
        # on the error, returning a more specific message to the user.
        return jsonify({"error": "Failed to generate motivation. Please try again."}), 500

# ensuring the Flask development server runs when execute app.py directly.
if __name__ == '__main__':
    app.run(debug=True) 
