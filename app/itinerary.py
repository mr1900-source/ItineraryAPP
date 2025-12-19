"""Functions to interact with the Gemini API to generate itineraries.

This module loads GEMINI_API_KEY from environment variables (use a .env file
during development). It exposes `generate_itinerary(prompt: str) -> str`.

The real network call is isolated here so tests can mock it.
"""
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
    """Return a dictionary to configure the Gemini API call.

    The assistant's guidance is passed as a 'system_instruction' in the
    configuration, and the user prompt is passed as 'contents'.
    """
    system_instruction = (
        "You are a professional travel itinerary planner. Create detailed, "
        "well-structured itineraries that are easy to read and follow. "
        "For each day and activity, include timing, descriptions, costs, and "
        "transportation suggestions where relevant. Be specific and practical."
    )

    user_content = f"Create a detailed itinerary based on: {user_prompt}"

    return {
        "system_instruction": system_instruction,
        "user_content": user_content,
    }


def _call_gemini_api(api_params: dict) -> str:
    """Call the Gemini API and return the model's text response.

    Raises ItineraryError if the API call fails or if credentials are missing.
    """
    if not GEMINI_API_KEY:
        raise ItineraryError('GEMINI_API_KEY not set in environment')

    try:
        client = genai.Client()
    except Exception as e:
        raise ItineraryError(f'Error creating Gemini client: {e}') from e

    config = types.GenerateContentConfig(
        system_instruction=api_params["system_instruction"],
        max_output_tokens=2000,
        temperature=0.7,
    )

    try:
        response = client.models.generate_content(
            model='gemini-2.0-flash-exp',
            contents=api_params["user_content"],
            config=config,
        )
        return response.text.strip()
    except Exception as e:
        raise ItineraryError(f"Gemini API call failed: {e}") from e


def generate_itinerary(user_prompt: str) -> str:
    """Public function: given a natural-language prompt return itinerary text.

    Args:
        user_prompt: Natural language description of travel plans
        
    Returns:
        Plain text itinerary
        
    Raises:
        ItineraryError: On empty prompt or API failures
    """
    if not user_prompt or not user_prompt.strip():
        raise ItineraryError('Empty prompt provided')

    api_params = _build_messages(user_prompt)
    return _call_gemini_api(api_params)