# 🎙️ VoiceBot App — Powered by AI 🤖

Welcome to **VoiceBot App**, an AI-powered chatbot with voice capabilities built using **Python**, **Streamlit**, and **OpenAI**. This project allows users to interact with a chatbot through speech input and get intelligent responses in real-time!

---

## 📦 Features

- 🎤 Voice input recognition
- 💬 AI-generated responses
- ⚙️ Streamlit web interface
- 🐳 Docker support for containerization
- 🔒 Environment variable management with `.env`

---

## 🚀 How to Run This Project

### 🔧 Requirements

Before you begin, make sure you have the following installed:

- [Python 3.10+](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/products/docker-desktop)
- A valid OpenAI API key (add it in your `.env` file)

---

### 🛠️ Run Locally (without Docker)

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/voicebot-app.git
   cd voicebot-app
### create envoriment 
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
### install dependices 
pip install -r requirements.txt
Add Environment Variables
Create a .env file and add:
OPENAI_API_KEY=your_openai_key_here
##Run the App
streamlit run voice.py
##🐳 Run with Docker
##Build Docker Image
docker build -t voicebot-app .
Run the Container
docker run --env-file .env -p 8501:8501 voicebot-app
To auto-reload with changes (live updates)
docker run --env-file .env -p 8501:8501 -v ${PWD}:/app voicebot-app  # On Windows: use full path instead of ${PWD}
📁 Project Structure
voicebot-app/
│
├── voice.py              # Main Streamlit app
├── requirements.txt      # Python dependencies
├── Dockerfile            
├── .dockerignore         
├── .env                  
├── README.md            
└── LICENSE               
📜 License
This project is licensed under the MIT License.

🙌 Author
Made with ❤️ by Ghulam Mustafa

Connect with me on LinkedIn
GitHub: ghulamMustafa
![image](https://github.com/user-attachments/assets/1fa3e515-c678-42c1-a8a8-794b9dde3057)
![image](https://github.com/user-attachments/assets/423918f8-1f28-4b8c-8d86-6a92b9bc3bab)
![image](https://github.com/user-attachments/assets/6d3f52c8-3885-4ddd-93c7-9d7b44fed338)












