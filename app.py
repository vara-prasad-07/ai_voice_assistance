from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os

# Initialize Flask app
app = Flask(__name__)
# Enable CORS for all domains on all routes
CORS(app)

# Configure Gemini API
genai.configure(api_key="AIzaSyCjBLyOTr-JES2woUKBPBoNB8uyaaCOObc")

@app.route('/generate', methods=['POST'])
def generate():
    try:
        # Get the prompt from the request
        data = request.json
        prompt = data.get('prompt', '')
        
        # Generate content using Gemini
        response = genai.GenerativeModel('gemini-2.0-flash').generate_content(prompt)
        
        # Return the response
        return jsonify({"data": [response.text]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Run the Flask app on localhost:5000
    app.run(debug=True, host='0.0.0.0', port=5000)