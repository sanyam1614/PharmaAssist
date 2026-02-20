import streamlit as st
from src.services.medical_ai import MedicalAIService
from src.services.audio import AudioService
from config.settings import AUDIO_FILENAME

# --- Page Setup ---
st.set_page_config(page_title="PharmaAssist", page_icon="🤖", layout="wide")
st.header("🤖 PharmaAssist: Medicines made simple!", divider="rainbow")

# --- Initialize Services ---
ai_service = MedicalAIService()
audio_service = AudioService()

# --- Session State ---
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "How can I help you with medication information today?"},
    ]

# --- Sidebar ---
with st.sidebar:
    st.title("ℹ️ About PharmaAssist")
    st.info("""
    PharmaAssist uses **Perplexity's Sonar API** to provide accurate, 
    up-to-date pharmaceutical information from trusted medical sources.
    
    **Features:**
    - 🔍 Real-time medical database search
    - 📚 Cited sources from authoritative organizations
    - 🔊 Text-to-speech output
    - 💾 Downloadable conversation history
    - 💬 Multi-turn conversation support
    """)
    
    st.warning("""
    **⚠️ Medical Disclaimer**
    
    This tool is for **informational purposes only**. 
    Always consult qualified healthcare professionals 
    for medical advice, diagnosis, or treatment.
    """)
    
    st.subheader("Conversation Management")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🗑️ Clear Chat", use_container_width=True):
            st.session_state.messages = [
                {"role": "assistant", "content": "How can I help you with medication information today?"}
            ]
            st.rerun()
    with col2:
        msg_count = len([m for m in st.session_state.messages if m["role"] == "user"])
        st.metric("Queries", msg_count)
    
    st.divider()
    st.subheader("📖 Trusted Resources")
    st.markdown("""
    - [FDA Drug Database](https://www.fda.gov/drugs)
    - [MedlinePlus](https://medlineplus.gov/)
    - [Drugs.com](https://www.drugs.com/)
    - [NIH](https://www.nih.gov/)
    - [WHO Medicines](https://www.who.int/health-topics/medicines)
    """)

# --- Chat Display ---
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# --- User Input ---
text_input = st.chat_input("Type the name of the medication")

if text_input:
    # Update state and display user message
    st.session_state.messages.append({"role": "user", "content": text_input})
    st.chat_message("user").write(text_input)

    # Generate AI Response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        with st.spinner("Searching medical databases and generating response..."):
            for chunk in ai_service.generate_response_stream(st.session_state.messages, text_input):
                full_response += chunk
                message_placeholder.markdown(full_response + "▌")
            
            message_placeholder.markdown(full_response)

        # Update session state
        st.session_state.messages.append({"role": "assistant", "content": full_response})

        # Generate Voice Output
        if full_response and not full_response.startswith("⚠️"):
            with st.spinner("Generating voice output..."):
                if audio_service.generate_audio(full_response):
                    st.audio(AUDIO_FILENAME)
                else:
                    st.warning("Could not generate audio output.")

        # Download Button
        st.divider()
        conversation_text = "\n\n".join([
            f"{msg['role'].upper()}: {msg['content']}" 
            for msg in st.session_state.messages
        ])
        
        st.download_button(
            label="📥 Download Conversation as TXT",
            data=conversation_text,
            file_name=f"pharmaassist_{text_input.replace(' ', '_')[:30]}.txt",
            mime="text/plain"
        )
