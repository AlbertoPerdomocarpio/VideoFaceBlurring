from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = 'app/uploads'
    app.config['PROCESSED_FOLDER'] = 'app/processed'
    app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # Limite: 100MB
    
    from .routes import bp
    app.register_blueprint(bp)
    
    return app
