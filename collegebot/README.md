# College Receptionist Chatbot

## Project Description:
An AI-based chatbot designed to provide assistance to students, faculty, and visitors at Bharata Mata College of Commerce & Arts. Trained on a dataset tailored for college-related inquiries, this chatbot utilizes a feed-forward neural network for understanding and responding to user queries. The Natural Language Toolkit (NLTK) is employed for text preprocessing tasks such as tokenization, stemming, and bag-of-words creation. The chatbot is capable of providing information on college services, courses, admissions, events, and more. Its flexibility allows for adaptation to various purposes by modifying the dataset.

## Tools:
1. **Programming Language**: Python
2. **Dataset Format**: JSON
3. **Machine Learning Library**: PyTorch
4. **Natural Language Toolkit**: NLTK

## Project Details:
- **Dataset**: The `college_receptionist_intents.json` file contains the dataset used for training the model. It includes various intents like 'greetings', 'goodbye', 'admissions', 'courses', etc., each with multiple patterns and associated responses. The bot selects a random response based on the matched intent.
- **Data/Text Preprocessing**: The `nltk_utils.py` file handles preprocessing using NLTK, including tokenization, stemming, and creating a bag-of-words representation for text inputs.
- **Model**: Defined in `model.py`, the model uses PyTorch to construct a feed-forward neural network with one hidden layer, employing ReLU as the activation function.
- **Training**: The `train.py` script is responsible for training the model. It preprocesses the dataset and trains the model using hyperparameters like the number of epochs and learning rate, which can be adjusted. The model is trained on available CPU or GPU resources. Post-training, the model's state is saved to `college_receptionist_data.pth`.
- **Chat Interface**: The `app.py` serves as the main interface for the chatbot, loading the trained model and handling user interactions through a web-based interface. The chatbot continues to converse until the user types "quit" and provides contact information after three consecutive failed attempts to understand the user's query.

## Instructions to Run the Code:
1. Set up a Python environment (e.g., using conda or venv).
2. Install PyTorch according to your environment from [PyTorch.org](https://pytorch.org).
3. Install NLTK by running `pip install nltk` in the terminal.
4. For the first run, uncomment `nltk.download('punkt')` in `nltk_utils.py` to download necessary NLTK data.

## How to Use:
1. Start the Flask application by running `python app.py`.
2. Open a web browser and navigate to `http://127.0.0.1:5000` to interact with the chatbot.

## References:
1. [Natural Language Toolkit (NLTK)](https://www.nltk.org)
2. [PyTorch](https://pytorch.org)

## Contributing:
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License:
This project is licensed under the MIT License - see the LICENSE file for details.
