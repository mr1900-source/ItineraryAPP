# TripCraft - AI-Powered Itinerary Planner

TripCraft is a web application that uses Google's Gemini AI to generate personalized travel itineraries. Simply describe your travel plans, and TripCraft creates a detailed, day-by-day itinerary with activities, timing, costs, and transportation suggestions.

## Features

- **AI-Powered Generation**: Uses Google Gemini API to create intelligent, personalized itineraries
- **Beautiful UI**: Professional Bootstrap 5 design with responsive layout
- **Save & Manage**: Store your favorite itineraries for future reference
- **Regenerate**: Create new variations of saved itineraries with one click
- **Formatted Display**: Itineraries are presented in an easy-to-read timeline format with icons and badges

## Prerequisites

- Python 3.10 or higher
- Anaconda (recommended) or Python virtual environment
- Google Gemini API key ([Get one here](https://aistudio.google.com/app/apikey))

## Installation

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd <your-repo-name>
```

### 2. Create Virtual Environment

Using Anaconda (recommended):

```bash
conda create -n tripcraft python=3.10
conda activate tripcraft
```

Or using venv:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory of the project:

```bash
touch .env  # On Windows: type nul > .env
```

Add the following content to your `.env` file:

```env
# Required: Your Google Gemini API key
GEMINI_API_KEY=your_api_key_here

# Required: Flask secret key (use any random string)
SECRET_KEY=your_secret_key_here
```

**To get a Gemini API key:**
1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the key and paste it into your `.env` file

**For the SECRET_KEY**, you can generate a random string using Python:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

### 5. Verify Installation

Run the tests to ensure everything is set up correctly:

```bash
pytest
```

All tests should pass ✅

## Usage

### Running the Application

Start the Flask development server:

```bash
python run.py
```

The application will be available at `http://127.0.0.1:5000`

### Using TripCraft

1. **Generate an Itinerary**
   - Enter a description of your trip in the text box
   - Include details like: destination, duration, budget, interests, preferences
   - Example: "A 3-day romantic weekend in Paris for two people, budget $800, interested in museums, cafes, and evening walks"
   - Click "Generate Itinerary"

2. **View Your Itinerary**
   - The AI will create a detailed itinerary with day-by-day activities
   - Each activity includes timing, description, cost estimates, and transportation notes

3. **Save Your Itinerary**
   - Give your itinerary a memorable title
   - Click "Save Itinerary"
   - Access it anytime from the "Saved Itineraries" page

4. **Manage Saved Itineraries**
   - View all saved itineraries from the navigation menu
   - Regenerate new versions based on the original prompt
   - Delete itineraries you no longer need

## Testing

Run all tests:

```bash
pytest
```

Run tests with verbose output:

```bash
pytest -v
```

Run tests with coverage report:

```bash
pytest --cov=app
```

### Test Structure

- `tests/test_itinerary.py`: Tests for AI generation and formatting functions
- `tests/test_storage.py`: Tests for save/load/delete operations

## Project Structure

```
tripcraft/
├── app/
│   ├── templates/
│   │   ├── base.html          # Base template with navbar/footer
│   │   ├── index.html         # Home page with generation form
│   │   ├── saved.html         # Saved itineraries list
│   │   └── view.html          # Individual itinerary view
│   ├── __init__.py            # Flask app factory
│   ├── itinerary.py           # Gemini API integration
│   ├── routes.py              # Flask routes/endpoints
│   └── storage.py             # JSON file storage operations
├── tests/
│   ├── test_itinerary.py      # Itinerary generation tests
│   └── test_storage.py        # Storage function tests
├── .github/
│   └── workflows/
│       └── pytest.yml         # GitHub Actions CI configuration
├── .env                       # Environment variables (not in git)
├── .gitignore                 # Git ignore rules
├── requirements.txt           # Python dependencies
├── run.py                     # Application entry point
└── README.md                  # This file
```

## Continuous Integration

This project uses GitHub Actions for automated testing. Every push and pull request triggers:

1. Python environment setup
2. Dependency installation
3. Pytest execution

View build status in the "Actions" tab of your GitHub repository.

## Technologies Used

- **Backend**: Python 3.10, Flask 2.0+
- **AI**: Google Gemini API (gemini-2.0-flash-exp model)
- **Frontend**: Bootstrap 5, Bootstrap Icons, HTML5
- **Testing**: Pytest 7.0+
- **CI/CD**: GitHub Actions
- **Storage**: JSON file-based persistence

## Troubleshooting

### "GEMINI_API_KEY not set in environment"

Make sure your `.env` file exists and contains your API key. Verify the file is in the root directory of the project.

### Tests Failing

If tests fail, ensure:
1. Virtual environment is activated
2. All dependencies are installed (`pip install -r requirements.txt`)
3. You're running pytest from the project root directory

### Port 5000 Already in Use

If port 5000 is already in use, you can change it in `run.py`:

```python
app.run(debug=True, host='127.0.0.1', port=5001)  # Change to any free port
```

### Itinerary Not Generating

- Verify your Gemini API key is valid
- Check your internet connection
- Review error messages in flash alerts
- Check the terminal for detailed error logs

## Future Enhancements

Potential features for future versions:

- Export itineraries to PDF
- Share itineraries via link
- Multiple language support
- Map integration
- Collaborative trip planning
- Budget tracking
- Weather integration
- Google Sheets integration for structured data storage

## License

This project is available under the MIT License. See `LICENSE` file for details.

## Contributing

This is a student project for an intro Python class. While contributions are welcome, please note this is primarily for educational purposes.

## Support

For issues or questions:
1. Check the Troubleshooting section above
2. Review error messages carefully
3. Consult your instructor
4. Check the [Gemini API documentation](https://ai.google.dev/docs)

## Acknowledgments

- Built with [Flask](https://flask.palletsprojects.com/)
- Powered by [Google Gemini AI](https://ai.google.dev/)
- Styled with [Bootstrap 5](https://getbootstrap.com/)
- Icons from [Bootstrap Icons](https://icons.getbootstrap.com/)

---