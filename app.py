from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

responses = {
    "hi": "Hello! 👋",
    "hello": "Hi there!",
    "how are you?": "I'm just a bot, but I'm doing great. How about you?",
    "what's your name?": "I'm ChatBot 1.0 🤖",
    "bye": "Goodbye! Have a nice day 😊"
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message'].lower()
    reply = responses.get(user_input, "Sorry, I didn't understand that.")
    return jsonify({'response': reply})

if __name__ == '__main__':
    app.run(debug=True)
