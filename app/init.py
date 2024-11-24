from flask import Flask
from app.routes import portfolio, marketdata
import os

def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object('app.config.Config')

    # Register blueprints
    app.register_blueprint(portfolio.bp)
    app.register_blueprint(marketdata.bp)

    return app
