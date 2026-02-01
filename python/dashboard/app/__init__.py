from flask import Flask
from app.config import Config
from app.api.vix import vix_bp
from app.api.pcr import pcr_bp
from app.api.rsi import rsi_bp

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Register blueprints
    app.register_blueprint(vix_bp, url_prefix="/api")
    app.register_blueprint(pcr_bp, url_prefix="/api")
    app.register_blueprint(rsi_bp, url_prefix="/api")

    return app
