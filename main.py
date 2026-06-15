from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
from google import genai
from datetime import datetime
import pytz

load_dotenv()

API_KEY = os.environ.get("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("GOOGLE_API_KEY not found")

client = genai.Client(api_key=API_KEY)

app = Flask(__name__)

def load_knowledge_base():

    with open("knowledge_base", "r", encoding="utf-8") as file:
        return file.read()

@app.route("/")
def home():
    return "AI FAQ TRIAGE RUNNING"

@app.route("/ask", methods=["POST"])
def ask():

    data = request.get_json()

    name = data.get("name", "No Name")
    email = data.get("email", "No Email")
    question = data.get("question", "No Question")
    ist = pytz.timezone("Asia/Kolkata")
    timestamp = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S")

    knowledge = load_knowledge_base()

    prompt = f"""
    Return ONLY valid JSON.

    You are a customer support assistant.

    Knowledge Base:
    {knowledge}

    Customer Question:
    {question}

    Rules:

    1. Answer ONLY using information present in the Knowledge Base.
    2. Do NOT guess.
    3. Do NOT assume.
    4. Do NOT make up policies or information.
    5. If the Knowledge Base does not contain enough information, mark it for human review.
    6. When answering, write a professional customer support email.
    7. Do not wrap the response in markdown or ```json blocks.

    If the question can be answered completely using the Knowledge Base, return:

    {{
        "status": "Answered by AI",
        "answer": "A professional customer support reply addressed to the customer.Dont add slash n to answer."
    }}

    If the question cannot be answered completely using the Knowledge Base, return:

    {{
        "status": "Needs Human Review",
        "answer": "                     -                    "
    }}

    Return JSON only.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    try:
        import json

        result = json.loads(response.text)

        status = result.get("status","Status not generated")
        answer = result.get("answer","Answer not generated")


    except Exception as e:
        return jsonify({
            "error": "Gemini response failed",
            "details": str(e),
            "raw_response": response.text
        }), 500

    return jsonify({
        "name": name,
        "email": email,
        "question": question,
        "answer": answer,
        "status": status,
        "timestamp": timestamp
    })



if __name__ == "__main__":
    app.run(debug=True, port=5000)
