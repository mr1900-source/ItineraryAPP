"""Functions to interact with the Gemini API to generate itineraries."""
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')

class ItineraryError(Exception):
    """Custom exception for itinerary generation errors."""
    pass

def _build_messages(user_prompt: str) -> dict:
    system_instruction = (
        "Create a travel itinerary. Use this exact format:\n"
        "OVERVIEW: [Summary]\n"
        "STOP: [Title] | [Description]\n"
        "TIPS: [Extra advice]"
    )
    user_content = f"Create an itinerary for: {user_prompt}"
    return {"system_instruction": system_instruction, "user_content": user_content}

def _call_gemini_api(api_params: dict) -> str:
    if not GEMINI_API_KEY:
        raise ItineraryError('GEMINI_API_KEY not set in environment')

    try:
        client = genai.Client()
        config = types.GenerateContentConfig(
            system_instruction=api_params["system_instruction"],
            max_output_tokens=2000,
            temperature=0.8, # Slightly higher for more creativity
        )
        response = client.models.generate_content(
            model='gemini-2.0-flash-exp',
            contents=api_params["user_content"],
            config=config,
        )
        return response.text.strip()
    except Exception as e:
        raise ItineraryError(f"Gemini API call failed: {e}") from e

def generate_itinerary(user_prompt: str) -> str:
    if not user_prompt or not user_prompt.strip():
        raise ItineraryError('Empty prompt provided')

    api_params = _build_messages(user_prompt)
    return _call_gemini_api(api_params)