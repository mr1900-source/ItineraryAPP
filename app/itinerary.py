"""Functions to interact with the OpenAI API to generate itineraries.


This module loads GEMINI_API_KEY from environment variables (use a .env file
during development). It exposes `generate_itinerary(prompt: str) -> str`.


The real network call is isolated here so tests can mock it.
"""
import os
from dotenv import load_dotenv

# --- New/Updated Imports for Gemini API ---
from google import genai
from google.genai import types # Import types for configuration objects

load_dotenv()

# Note: The 'google-genai' SDK automatically looks for GEMINI_API_KEY
# or GOOGLE_API_KEY, so the client creation handles authentication.
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')


class ItineraryError(Exception):
    pass


def _build_messages(user_prompt: str) -> dict:
    """Return a dictionary to configure the Gemini API call.

    The assistant's guidance is passed as a 'system_instruction' in the
    configuration, and the user prompt is passed as 'contents'.
    """
    system_instruction = (
        "You are an assistant that writes concise, well-structured day/evening "
        "itineraries for a user. When relevant include timing, venue types, "
        "transport suggestions, and rough costs. Reply in plain text."
    )

    user_content = f"Create an itinerary based on: {user_prompt}"

    # Return a dictionary containing the separate prompt components
    return {
        "system_instruction": system_instruction,
        "user_content": user_content,
    }


def _call_gemini_api(api_params: dict) -> str:
    """Call the Gemini API and return the model's text response.

    This function replaces the old _call_openai_chat.
    """

    # --- Initialization ---
    if not GEMINI_API_KEY:
        raise ItineraryError('GEMINI_API_KEY not set in environment')

    # 1. Instantiate the Client (it automatically uses the environment variable)
    try:
        client = genai.Client()
    except Exception as e:
        raise ItineraryError(f'Error creating Gemini client: {e}') from e

    # 2. Configure the generation parameters
    config = types.GenerateContentConfig(
        # The 'system' message from the old API becomes a system_instruction
        system_instruction=api_params["system_instruction"],
        max_output_tokens=2000, # Matches the old max_tokens
        temperature=0.7,      # Matches the old temperature
    )

    # 3. Call the API
    try:
        # Use models.generate_content for a single, stateless request
        response = client.models.generate_content(
            model='gemini-2.5-flash', # A fast, capable model (equivalent to gpt-3.5-turbo)
            contents=api_params["user_content"],
            config=config,
        )

        # The response text is accessed directly
        return response.text.strip()

    except Exception as e:
        # Wrap any lower-level errors in ItineraryError for the caller
        raise ItineraryError(f"Gemini API call failed: {e}") from e


def generate_itinerary(user_prompt: str) -> str:
    """Public function: given a natural-language prompt return itinerary text.

    Raises ItineraryError on problems.
    """

    if not user_prompt or not user_prompt.strip():
        raise ItineraryError('Empty prompt provided')


    api_params = _build_messages(user_prompt)
    return _call_gemini_api(api_params)


# --- Example Usage ---
# if __name__ == '__main__':
#     prompt = "A romantic evening itinerary for two in Paris, starting at 7 PM with a budget of 150 EUR for dinner and transport."
#     try:
#         itinerary = generate_itinerary(prompt)
#         print("--- Generated Itinerary ---")
#         print(itinerary)
#     except ItineraryError as e:
#         print(f"An error occurred: {e}")