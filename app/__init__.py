"""Flask application factory."""
import os
from flask import Flask
from dotenv import load_dotenv

def create_app(test_config=None):
    # Load .env (if present) into environment variables
    load_dotenv()

    app = Flask(__name__, instance_relative_config=False)


    # Basic config
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY', 'dev-secret'),
    )

    # Import and register routes
    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app