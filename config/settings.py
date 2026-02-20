import streamlit as st

# API Configuration
PERPLEXITY_API_KEY = st.secrets.get("PERPLEXITY_API_KEY", "YOUR_PERPLEXITY_API_KEY")
PERPLEXITY_BASE_URL = "https://api.perplexity.ai"
MODEL_NAME = "sonar"

# Audio Settings
AUDIO_FILENAME = "Output_Audio.mp3"
DEFAULT_LANG = "en"

# Trusted Sources
TRUSTED_SOURCES = [
    "Centers for Disease Control and Prevention (CDC)",
    "ClinicalTrials.gov",
    "Food and Drug Administration (FDA)",
    "National Cancer Institute",
    "National Institutes of Health (NIH)",
    "National Library of Medicine",
    "World Health Organization (WHO)",
    "Indian Medical Association",
    "MedlinePlus (https://medlineplus.gov/)",
    "Drugs.com FDA Consumer (https://www.drugs.com/fda-consumer)",
    "WebMD Drugs Database (https://www.webmd.com/drugs/2/index)"
]

# Prompts
SYSTEM_PROMPT = f"""You are a helpful pharmaceutical and medical assistant that provides accurate and reliable information about medicines from trusted sources. 

Focus on searching and citing information from these authoritative sources:
{chr(10).join([f"- {source}" for source in TRUSTED_SOURCES])}

Provide detailed information with clear section divisions covering:
1. Generic and brand names
2. Active ingredients
3. Uses and indications
4. Side effects
5. Adverse reactions
6. Drug interactions (with medications, foods, substances)
7. Precautions and warnings
8. Dosage forms and administration
9. Storage requirements

if multiple medicines are provided, interactions between them.

Always cite your sources and provide links for further reading."""

def get_user_query_prompt(medicine_name: str) -> str:
    return f"""Give a comprehensive, detailed description about the following medicine: {medicine_name}

Please include:
- Generic name and common brand names
- Active ingredients and composition
- Primary uses and medical indications
- Common and serious side effects
- Potential adverse reactions
- Drug interactions (with other medications, foods, or substances)
- Precautions, contraindications, and warnings
- Available dosage forms and administration routes
- Proper storage requirements

Provide citations from authoritative medical sources."""
