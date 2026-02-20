# PharmaAssist Project Specification

## 1. Overview
PharmaAssist is a Streamlit-based pharmaceutical assistant that provides accurate and reliable information about medicines using the Perplexity Sonar API. It features multi-turn conversation support, text-to-speech output, and downloadable chat history.

## 2. Technical Stack
- **Frontend**: Streamlit
- **AI Engine**: Perplexity Sonar (via OpenAI SDK)
- **Voice Engine**: gTTS (Google Text-to-Speech)
- **Language**: Python 3.9+

## 3. Project Structure
The project follows a modular architecture:
```text
PharmaAssist/
├── app.py                # Main Entry Point (Streamlit UI)
├── config/
│   └── settings.py       # Configuration and Constants
├── src/
│   ├── services/
│   │   ├── medical_ai.py # Perplexity API Service
│   │   └── audio.py      # Audio Generation Service
│   └── utils/
│       └── helpers.py    # Formatting and common utilities
├── docs/
│   └── spec.md           # Project Specification
└── requirements.txt      # Dependency Management
```

## 4. Key Components

### 4.1 Configuration (config/settings.py)
- Manage API keys (from st.secrets).
- Define system prompts.
- List authoritative medical sources.
- Audio settings.

### 4.2 Medical AI Service (src/services/medical_ai.py)
- Class-based interface for interacting with Perplexity API.
- Handles conversation history and alternating message roles.
- Streaming support for UI feedback.

### 4.3 Audio Service (src/services/audio.py)
- Handles text cleaning (removing markdown/URLs).
- Generates and saves MP3 files using gTTS.
- Error handling for audio generation.

### 4.4 Main UI (app.py)
- Handles Streamlit page config and layout.
- Manages session state for chat messages.
- Coordinates between user input and services.

## 5. Functional Requirements
- **Medicine Search**: Users can type a medicine name and get a structured, cited report.
- **Audio Output**: AI responses are converted to speech and playable in-browser.
- **Download**: Users can download the full chat history as a `.txt` file.
- **History Management**: Users can clear the chat history.

## 6. Coding Standards
- Use type hints for all function signatures.
- Document classes and methods with docstrings.
- Follow PEP 8 style guidelines.
- Separate UI logic from business logic.
