import os
SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev'
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
import os
SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev'

class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///ecommerce.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False