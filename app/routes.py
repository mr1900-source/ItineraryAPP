"""HTTP routes for the itinerary app."""
from flask import Blueprint, render_template, request, redirect, url_for, flash
from .itinerary import generate_itinerary, ItineraryError


main_bp = Blueprint('main', __name__, template_folder='templates')

@main_bp.route('/', methods=['GET'])
def index():
# Simple page with a form
    return render_template('index.html')

@main_bp.route('/plan', methods=['POST'])
def plan():
    prompt = request.form.get('prompt', '').strip()
    if not prompt:
        flash('Please enter a prompt describing the itinerary you want.', 'warning')
        return redirect(url_for('main.index'))

    try:
        itinerary_text = generate_itinerary(prompt)
    except ItineraryError as e:
        flash(f'Error generating itinerary: {e}', 'danger')
        return redirect(url_for('main.index'))


    return render_template('index.html', prompt=prompt, itinerary=itinerary_text)