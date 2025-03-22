from flask import Flask, request, jsonify, render_template_string, send_from_directory
import torch
import json
import numpy as np
import random
from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

app = Flask(__name__)

# Load the trained model
FILE = "college_receptionist_data.pth"
data = torch.load(FILE, map_location=torch.device('cpu'))

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size)
model.load_state_dict(model_state)
model.eval()

# Load intents
with open('college_receptionist_intents.json', 'r') as f:
    intents = json.load(f)

@app.route("/")
def home():
    try:
        with open('ui/index.html', 'r', encoding='utf-8') as file:
            index_html = file.read()
        return render_template_string(index_html)
    except Exception as e:
        return str(e)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({"response": "Please type something."})

    sentence = tokenize(user_input)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X)

    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]

    # Debugging print statement
    print(f"Predicted tag: {tag}")

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                response = random.choice(intent['responses'])
                return jsonify({"response": response})
    else:
        return jsonify({"response": "I do not understand..."})

@app.route('/ui/<path:filename>')
def custom_static(filename):
    return send_from_directory('ui', filename)

if __name__ == "__main__":
    app.run(debug=True)