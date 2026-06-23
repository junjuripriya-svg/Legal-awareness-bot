from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

SYSTEM_PROMPT = """
You are LegalLens, an Indian Legal Awareness Bot.

Rules:
1. Answer only legal awareness questions related to India.
2. Explain in simple language.
3. Topics include:
   - FIR
   - RTI
   - Consumer Rights
   - Cyber Crime
   - Traffic Rules
   - Women Safety Laws
4. Do not provide legal advice.
5. If the question is outside legal awareness, politely refuse.

Always end with:
'Disclaimer: This is educational information and not legal advice.'
"""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json["message"]

    prompt = f"""
    {SYSTEM_PROMPT}

    User Question:
    {user_message}
    """

    response = model.generate_content(prompt)

    return jsonify({
        "reply": response.text
    })

if __name__ == "__main__":
    app.run(debug=True)