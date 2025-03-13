from flask import Flask, render_template, request, jsonify
from chatbot import get_response
import os

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route("/")
def index():
    
    print(os.environ.get("GEMINI_API_KEY")) 
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def ask():
    user_input = request.json.get("message")
    response = get_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
