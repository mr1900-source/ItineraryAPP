"""Pytest tests for the itinerary generation module.


These tests mock the Gemini call so they run quickly and don't require network.
"""

import pytest
from app import itinerary

class DummyResponse:
    def __init__(self, text):
        self.text = text

def test_generate_itinerary_success(monkeypatch):
    user_prompt = 'date night 6-9pm in downtown Manhattan, Italian, $60pp'


    def fake_call(api_params):
        # Return a fake itinerary string
        return '6:00 PM - Arrive; 6:30 PM - Dinner at Trattoria (approx $50pp)'

    monkeypatch.setattr(itinerary, '_call_gemini_api', fake_call)

    result = itinerary.generate_itinerary(user_prompt)
    assert '6:00 PM' in result or 'dinner' in result.lower()

def test_generate_itinerary_empty_prompt():
    with pytest.raises(itinerary.ItineraryError):
        itinerary.generate_itinerary('')