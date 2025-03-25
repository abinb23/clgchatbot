import random
import json
import torch
import speech_recognition as sr
from gtts import gTTS
import os

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Load the college receptionist intents
with open('college_receptionist_intents.json', 'r') as json_data:
    intents = json.load(json_data)

# Load the trained model
FILE = "college_receptionist_data.pth"
data = torch.load(FILE, map_location=torch.device('cpu'))

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "ReceptionBot"
print("Welcome to Bharata Mata College of Commerce & Arts. I am your receptionist bot. Let's chat! (type 'quit' to exit)")


def get_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            print(f"You (Voice): {text}")
            return text.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Could you repeat?")
            return None
        except sr.RequestError:
            print("API request error. Please check your internet connection.")
            return None


def speak(text):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    os.system("start response.mp3")


flag = 0
while True:
    print("\nChoose input mode: (1) Type (2) Speak")
    mode = input("Enter 1 or 2: ")
    if mode == "1":
        sentence = input("You: ")
    elif mode == "2":
        sentence = get_audio()
        if not sentence:
            continue
    else:
        print("Invalid choice. Please select again.")
        continue

    if sentence == "quit":
        break

    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        flag = 0
        for intent in intents['intents']:
            if tag == intent["tag"]:
                response = random.choice(intent['responses'])
                print(f"{bot_name}: {response}")
                speak(response)
    else:
        print(f"{bot_name}: I do not understand...please check the website")
        speak("I do not understand...please check the website")
        flag += 1
        if flag == 3:
            contact_info = "Please try to Contact us. Telephone: +8802985910454. Email: info@grandbangladeshhotel.com"
            print(contact_info)
            speak(contact_info)
            flag = 0