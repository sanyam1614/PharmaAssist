from openai import OpenAI
from typing import List, Dict, Generator, Any
from config.settings import PERPLEXITY_API_KEY, PERPLEXITY_BASE_URL, MODEL_NAME, SYSTEM_PROMPT, get_user_query_prompt

class MedicalAIService:
    """Service to handle interactions with the Perplexity AI API."""
    
    def __init__(self):
        self.client = OpenAI(
            api_key=PERPLEXITY_API_KEY,
            base_url=PERPLEXITY_BASE_URL
        )
        self.system_message = {"role": "system", "content": SYSTEM_PROMPT}

    def generate_response_stream(self, message_history: List[Dict[str, str]], medicine_name: str) -> Generator[str, Any, None]:
        """
        Generates a streaming response from the AI.
        
        Args:
            message_history: List of previous chat messages.
            medicine_name: Name of the medicine to query.
            
        Yields:
            Chunks of the generated response text.
        """
        conversation_messages = [self.system_message]
        
        # Build conversation history ensuring alternation for Perplexity
        # Filter out the initial assistant greeting and take last 8 messages
        chat_history = [msg for msg in message_history 
                        if not (msg["role"] == "assistant" and 
                               msg["content"] == "How can I help you with medication information today?")]
        
        recent_history = chat_history[-9:-1] if len(chat_history) > 9 else chat_history[:-1]
        
        for msg in recent_history:
            conversation_messages.append({
                "role": msg["role"],
                "content": msg["content"]
            })
            
        # Add current query
        current_query = {
            "role": "user",
            "content": get_user_query_prompt(medicine_name)
        }
        conversation_messages.append(current_query)

        try:
            stream = self.client.chat.completions.create(
                model=MODEL_NAME,
                messages=conversation_messages,
                stream=True,
                temperature=0.2,
                max_tokens=2048,
                top_p=0.9
            )
            
            for chunk in stream:
                if chunk.choices and chunk.choices[0].delta.content:
                    yield chunk.choices[0].delta.content
                    
        except Exception as e:
            yield f"⚠️ Error generating response: {str(e)}"
