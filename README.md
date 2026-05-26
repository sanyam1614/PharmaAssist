# 🤖 PharmaAssist — Medicines Made Simple

PharmaAssist is an AI-powered pharmaceutical information chatbot built with **Streamlit** and **Perplexity's Sonar API**. It provides accurate, cited, real-time medication information sourced from trusted medical databases — with voice output and conversation download support.

> ⚠️ **Medical Disclaimer:** This tool is for informational purposes only. Always consult a qualified healthcare professional for medical advice, diagnosis, or treatment.

---

## ✨ Features

- 🔍 **Real-time medical search** — powered by Perplexity's Sonar API for up-to-date pharmaceutical data
- 📚 **Cited sources** — responses backed by authoritative organizations (FDA, NIH, WHO, MedlinePlus, Drugs.com)
- 🔊 **Text-to-speech output** — converts AI responses to audio using gTTS
- 💾 **Downloadable conversation history** — export your chat as a `.txt` file
- 💬 **Multi-turn conversation** — maintains context across the entire session
- 🗑️ **Chat management** — clear history and track query count from the sidebar

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | [Streamlit](https://streamlit.io/) |
| AI / LLM | [Perplexity Sonar API](https://www.perplexity.ai/) (via OpenAI-compatible client) |
| Text-to-Speech | [gTTS (Google Text-to-Speech)](https://gtts.readthedocs.io/) |
| Language | Python 3.9+ |
| Testing | pytest |

---

## 📁 Project Structure

```
PharmaAssist/
├── app.py                  # Main Streamlit application entry point
├── requirements.txt        # Python dependencies
├── config/
│   └── settings.py         # App configuration (API keys, filenames, etc.)
├── src/
│   └── services/
│       ├── medical_ai.py   # Perplexity Sonar API integration & streaming
│       └── audio.py        # gTTS audio generation service
└── docs/                   # Additional documentation
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- A [Perplexity API key](https://www.perplexity.ai/)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/sanyam1614/PharmaAssist.git
   cd PharmaAssist
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your API key**

   Open `config/settings.py` and add your Perplexity API key:
   ```python
   PERPLEXITY_API_KEY = "your_api_key_here"
   ```

   Or set it as an environment variable:
   ```bash
   export PERPLEXITY_API_KEY="your_api_key_here"
   ```

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

5. Open your browser and navigate to `http://localhost:8501`

---

## 💡 Usage

1. Type the name of a medication or a pharmaceutical question in the chat input.
2. PharmaAssist will search medical databases and stream a cited response.
3. An audio version of the response will auto-play in the chat.
4. Use the **Download Conversation** button to export the session as a `.txt` file.
5. Use the **Clear Chat** button in the sidebar to start a fresh session.

---

## 📦 Dependencies

```
streamlit>=1.30.0
gTTS>=2.5.0
openai>=1.10.0
pytest>=8.0.0
```

---

## 🧪 Running Tests

```bash
pytest
```

---

## 📖 Trusted Medical Sources

PharmaAssist pulls information from:

- [FDA Drug Database](https://www.fda.gov/drugs)
- [MedlinePlus](https://medlineplus.gov/)
- [Drugs.com](https://www.drugs.com/)
- [NIH](https://www.nih.gov/)
- [WHO Medicines](https://www.who.int/health-topics/medicines)

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

---

## 📄 License

This project is open source. See the [LICENSE](LICENSE) file for details.

---

*Built with ❤️ by [sanyam1614](https://github.com/sanyam1614)*
