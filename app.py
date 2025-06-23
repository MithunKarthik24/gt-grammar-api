
from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def home():
    return "✅ GPT Grammar API is running!"

@app.route('/fix', methods=['GET'])
def fix_grammar():
    text = request.args.get('text', '')

    if not text.strip():
        return jsonify(error="Text input is empty."), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that fixes grammar in sentences."},
                {"role": "user", "content": f"Fix this sentence: {text}"}
            ],
            temperature=0.3,
            max_tokens=100
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        return jsonify(error=str(e)), 500
