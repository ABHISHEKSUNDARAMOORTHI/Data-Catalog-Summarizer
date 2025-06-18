
import os
import google.generativeai as genai
from dotenv import load_dotenv, find_dotenv
import json


dotenv_path = find_dotenv()
if dotenv_path:
    load_dotenv(dotenv_path)

GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")


if not GOOGLE_API_KEY or GOOGLE_API_KEY == "YOUR_ACTUAL_GEMINI_API_KEY_HERE":
    raise RuntimeError(
        "❌ GEMINI_API_KEY not found or is the placeholder value in your .env file. "
        "Please set it correctly to use AI features. Refer to the README for setup instructions."
    )

_gemini_model_instance = None

def get_gemini_model():
    """
    Initializes and returns a Gemini GenerativeModel.
    Prioritizes cost-effective models. Ensures model is initialized only once.
    """
    global _gemini_model_instance
    if _gemini_model_instance is not None:
        return _gemini_model_instance

    genai.configure(api_key=GOOGLE_API_KEY)

    available_models = []
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            available_models.append(m.name)

    preferred_order = [
        'models/gemini-1.5-flash', 
        'models/gemini-pro',     
        'models/gemini-1.5-pro'   
    ]

    chosen_model_name = None
    for preferred_model in preferred_order:
        if preferred_model in available_models:
            chosen_model_name = preferred_model
            break
    
    if chosen_model_name is None and available_models:
        chosen_model_name = available_models[0] 

    if chosen_model_name:
        try:
            _gemini_model_instance = genai.GenerativeModel(chosen_model_name)
            print(f"Gemini model initialized: {chosen_model_name}")
            return _gemini_model_instance
        except Exception as e:
            raise Exception(f"Failed to initialize Gemini model '{chosen_model_name}'. Please check your API key and network access.") from e
    else:
        raise Exception(
            "No suitable Gemini model found that supports 'generateContent'. "
            "Please ensure your API key is correct and valid, or check Google AI Studio for available models."
        )


def ask_gemini_text(prompt: str) -> str:
    """
    Sends a given prompt to the initialized Gemini model for text generation and returns its text response.
    Returns Markdown-formatted text from the AI.
    """
    try:
        model_instance = get_gemini_model()
    except Exception as e:
        return f"❌ AI Service Error: {e}"

    if not prompt.strip():
        return "❌ Please provide a valid prompt for the AI to process."

    try:
        response = model_instance.generate_content(prompt)

        if response and response.candidates and len(response.candidates) > 0 and \
           response.candidates[0].content and response.candidates[0].content.parts and \
           len(response.candidates[0].content.parts) > 0:
            return response.candidates[0].content.parts[0].text
        else:
            print(f"Gemini API returned an empty or unexpected text response structure: {response}")
            return "❌ AI did not return a valid text response. The AI might have refused the query or an internal error occurred. Please try again with different or simpler code."
    except genai.types.BlockedPromptException as e:
        return f"❌ AI Blocked Content: Your request for text generation was blocked due to safety policy. Details: {e.response.prompt_feedback.block_reason.name}."
    except Exception as e:
        print(f"Error during Gemini text API call: {e}")
        return f"❌ Gemini Text API Call Failed: {e}. Possible issues: network problem, rate limit, or invalid API key/model access."

