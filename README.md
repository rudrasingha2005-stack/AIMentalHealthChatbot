🧠 Mental Health Support Chatbot

A simple AI-powered mental health support chatbot built using Python and the Google Gemini API.
The chatbot provides empathetic, non-judgmental responses to users and helps them express their thoughts in a safe conversational environment.

✨ Features

🤖 AI-generated supportive responses using Gemini 2.5 Flash Lite

💬 Interactive command-line chat interface

🧠 Empathetic and non-judgmental tone

⏱️ Short, concise replies (1–10 lines)

🔒 Easy to configure with your own API key

🚪 Exit anytime by typing endchat

🛠️ Tech Stack

Python

Google Generative AI (Gemini API)

CLI (Command Line Interface)

📂 Project Structure
mental-health-support-chatbot/
│
├── chatbot.py          # Main chatbot script
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies (optional)
⚙️ Installation
1️⃣ Clone the repository
git clone https://github.com/your-username/mental-health-support-chatbot.git
cd mental-health-support-chatbot
2️⃣ Create a virtual environment (recommended)
python -m venv venv

Activate it:

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate
3️⃣ Install dependencies
pip install google-genai
🔑 API Key Setup

Get your API key from Google AI Studio.

Then update this line in your code:

client = Client(api_key="YOUR_API_KEY_HERE")

⚠️ Do NOT upload your API key to GitHub.
Use environment variables for production:

setx GEMINI_API_KEY "your_api_key"

Then in Python:

import os
client = Client(api_key=os.getenv("GEMINI_API_KEY"))
▶️ How to Run
python chatbot.py

You will see:

WELCOME TO MENTAL HEALTH SUPPORT
I hope you are doing well today. Please tell me your thoughts (Type endchat to exit)

Start chatting!

Type:

endchat

to exit the program.

🧠 Example Conversation
user: I feel very stressed about my exams
Chatbot: It sounds like you're carrying a lot of pressure right now. Try taking a few slow breaths and breaking your study time into small, manageable steps. You're doing your best, and that matters. Would you like a simple relaxation technique?
⚠️ Disclaimer

This chatbot is not a substitute for professional mental health care.
If you are experiencing severe distress, please contact:

A licensed mental health professional

A trusted person

A local mental health helpline

🚀 Future Improvements

🌐 Web interface (React/Vite frontend)

🗂️ Chat history storage

🎯 Mood detection

🔊 Voice input/output

🛡️ Crisis response handling

👨‍💻 Author

Debjyoti Sinha
B.Tech Student | AI & Software Enthusiast

📜 License

This project is licensed under the MIT License.