# 🤖 Jarvis - Python Voice Assistant

Jarvis is a Python-based voice assistant that listens for the wake word **"Jarvis"** and performs various tasks such as opening websites, launching desktop applications, searching Google, telling the current time and date, answering simple "Who is" questions using Wikipedia, and playing songs from a custom music library.

This project was built to strengthen my Python programming skills and gain hands-on experience with speech recognition, text-to-speech, and automation.

---

## ✨ Features

- 🎙️ Wake word detection ("Jarvis")
- 🗣️ Speech recognition using Google Speech Recognition
- 🔊 Natural text-to-speech using Microsoft Edge TTS
- 🌐 Open popular websites
  - Google
  - YouTube
  - GitHub
  - ChatGPT
  - Instagram
  - Gmail
  - Spotify
- 🔍 Google Search
- 📖 Wikipedia search
- ⏰ Tell the current time
- 📅 Tell today's date
- 🖥️ Open desktop applications
  - Notepad
  - Calculator
  - Paint
  - Google Chrome
- 🎵 Play songs from a custom music library
- ⚡ Shutdown and restart the computer through voice commands

---

## 🛠️ Technologies Used

- Python 3
- SpeechRecognition
- Edge-TTS
- Pygame
- Wikipedia
- Asyncio
- Webbrowser
- OS
- Subprocess

---

## 📂 Project Structure

```
Jarvis-Voice-Assistant/
│
├── main.py
├── MusicLibrary.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📦 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Jarvis-Voice-Assistant.git
```

Go to the project folder

```bash
cd Jarvis-Voice-Assistant
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
python main.py
```

---

## 📋 Required Python Packages

```
SpeechRecognition
edge-tts
pygame
wikipedia
PyAudio
```

Install them manually if required:

```bash
pip install SpeechRecognition edge-tts pygame wikipedia PyAudio
```

---

## 🎤 Example Commands

Say:

```
Jarvis
```

Then give commands like:

- Open Google
- Open YouTube
- Open GitHub
- Open Chat
- Open Mail
- Open Spotify
- Open Notepad
- Open Calculator
- Open Paint
- Search Python programming
- Who is Elon Musk
- What is the time
- What is today's date
- Play Believer

---

## ⚠️ Notes

- This project currently works on **Windows**.
- Google Chrome path may need to be changed depending on your installation.
- Songs are played from a custom `MusicLibrary.py` file.
- Internet connection is required for speech recognition, Wikipedia search, and Edge-TTS.

---

## 🚀 Future Improvements

- Integrate OpenAI GPT for intelligent conversations
- Weather updates
- News headlines
- Voice authentication
- Smart home automation
- Email sending
- WhatsApp automation
- GUI using Tkinter or CustomTkinter
- Executable (.exe) version
- Better command handling with NLP

---

## 📸 Demo

You can add screenshots or a screen recording here later.

---

## 👨‍💻 Author

**Krishna Aggarwal**

B.Tech Computer Science Engineering Student

Passionate about Python, Artificial Intelligence, and Software Development.

---

## ⭐ Support

If you found this project useful, consider giving it a **⭐ Star** on GitHub.
