import os

class Config:
    SECRET_KEY = os.urandom(24)
    UPLOAD_FOLDER = 'app/uploads'
    PROCESSED_FOLDER = 'app/processed'
