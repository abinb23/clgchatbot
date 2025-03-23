Bharata Mata College of Commerce and Arts - Website & Chatbot
Project Overview
This project consists of:

A responsive website providing information about Bharata Mata College of Commerce and Arts (BMCCA).

An AI-powered chatbot, deployed separately and accessible from the website to assist students, faculty, and visitors with common queries.

Website & Chatbot Integration
How It Works
1️⃣ Deploy the chatbot first (so it can be accessed via the website).
2️⃣ Run the website, which redirects users to the chatbot for queries.

Technologies Used
Frontend: HTML, CSS, JavaScript

Backend: Python (Flask for chatbot)

Machine Learning: PyTorch (for chatbot)

Natural Language Processing (NLP): NLTK

Hosting/Deployment: npm (for chatbot), Live Server (for website)

Step 1: Deploy the Chatbot
Install Dependencies
Ensure Python and Node.js are installed, then run:

bash
Copy
Edit
pip install flask torch nltk speechrecognition gtts
npm install
Download NLTK Data
Run the following in Python:

python
Copy
Edit
import nltk
nltk.download('punkt')
Train the Model (if needed)
bash
Copy
Edit
python train.py
Run the Chatbot Server
Start the Flask Server

bash
Copy
Edit
python app.py
This will start the chatbot at http://127.0.0.1:5000

Deploy Chatbot Using npm (if needed)

bash
Copy
Edit
npm start
The chatbot will now be accessible for integration with the website.

Step 2: Run the Website
How to Set Up the Website
Ensure the chatbot is running at http://127.0.0.1:5000.

Download or clone this repository.

Open the project folder in VS Code.

Install the Live Server extension if not already installed.

Right-click index.html and select "Open with Live Server".

The website will open in your browser, and the chatbot link will now work.

File Structure
bash
Copy
Edit
/project
│── index.html          # Website main page  
│── styles.css          # CSS file for styling  
│── script.js           # JavaScript functionalities  
│── /images             # Folder for college images  
│── /assets             # Additional resources (if any)  
│── app.py              # Flask application (chatbot interface)  
│── chat.py             # Handles text and voice input  
│── college_receptionist_intents.json   # Chatbot intents & responses  
│── model.py            # Neural network architecture  
│── nltk_utils.py       # NLP utility functions  
│── train.py            # Training script  
│── package.json        # npm configuration for chatbot deployment  
│── server.js           # Node.js file for deploying chatbot  
│── README.md           # Project documentation  
│── /ui                 # UI files (HTML & static content)  
Mission & Core Values
Our Mission
BMCCA aims to equip the young generation with personal and professional excellence, as well as social commitment, to meet global challenges through:
✅ Continuous teaching-learning-training programs.
✅ Value-based activities for overall development.

Core Values
✔ Respect for All
✔ Integrity & Honesty
✔ Innovation & Creativity
✔ Relentless Passion for Excellence
✔ Quality as a Continuous Process

Quality Policy
Our goal is to maintain exemplary standards in education by:

Structured coaching system

Competitive and committed faculty

Effective teaching & evaluation

Continuous improvement for student success

Future Enhancements
🚀 Website Improvements
✅ Responsive Design: Optimized for mobile & tablet users.
✅ SEO Optimization: Improve online visibility.
✅ Student Portal: Add a contact form & login system.

🤖 Chatbot Upgrades
✅ Voice Interaction: Enable speech-based queries.
✅ More FAQs: Improve accuracy with additional data.
✅ Deployment on Cloud: Host chatbot using npm & cloud services.

Contributing
Pull requests are welcome! If you want to suggest improvements, please open an issue to discuss your idea before submitting a major change.

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Acknowledgments
🙏 Thanks to Bharata Mata College for their support.
🚀 Special thanks to the developers of PyTorch, NLTK, Flask, JavaScript, and npm for their amazing tools.

✅ Now, the chatbot is deployed first before the website runs, ensuring proper redirection! 🚀 Let me know if you need any tweaks! 🎯
