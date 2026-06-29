from flask import Flask, render_template, request, jsonify
from chatbot import FAQChatbot


app = Flask(__name__)


chatbot = FAQChatbot()


@app.route("/")
def home():
    """
    Render chatbot homepage
    """
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():

    data = request.get_json()

    if not data:
        return jsonify({
            "answer": "Invalid request.",
            "confidence": 0
        })

    user_question = data.get("question", "").strip()

    if user_question == "":
        return jsonify({
            "answer": "Please enter a question.",
            "confidence": 0
        })

    answer, confidence = chatbot.get_answer(user_question)

    return jsonify({
        "question": user_question,
        "answer": answer,
        "confidence": round(float(confidence), 2)
    })


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "error": "Page not found"
    }), 404


@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        "error": "Internal Server Error"
    }), 500


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )