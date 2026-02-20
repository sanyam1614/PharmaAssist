import re
from gtts import gTTS
from config.settings import AUDIO_FILENAME, DEFAULT_LANG

class AudioService:
    """Service to handle text-to-speech generation."""
    
    @staticmethod
    def clean_text(text: str) -> str:
        """
        Removes markdown formatting and URLs for cleaner audio output.
        
        Args:
            text: The text to clean.
            
        Returns:
            Cleaned text.
        """
        # Remove markdown formatting
        text = text.replace("**", "").replace("##", "")
        # Remove URLs
        text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text)
        return text

    def generate_audio(self, text: str) -> bool:
        """
        Generates an MP3 file from text.
        
        Args:
            text: The text to convert to speech.
            
        Returns:
            True if successful, False otherwise.
        """
        try:
            cleaned_text = self.clean_text(text)
            if not cleaned_text.strip():
                return False
                
            speech = gTTS(text=cleaned_text, lang=DEFAULT_LANG, slow=False)
            speech.save(AUDIO_FILENAME)
            return True
        except Exception:
            return False
