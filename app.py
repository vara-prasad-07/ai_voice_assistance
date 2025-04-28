from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os

# Initialize Flask app
app = Flask(__name__)
# Enable CORS for all domains on all routes
CORS(app)

# Configure Gemini API
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set.")
genai.configure(api_key=api_key)

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.json
        prompt = data.get('prompt', '')
        response = genai.GenerativeModel('gemini-2.0-flash').generate_content(prompt)
        return jsonify({"data": [response.text]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Local testing only. In Render, gunicorn will handle it.
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
