from flask import Flask
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, current_user, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
import os
from config import *

app = Flask(__name__)
app.config.from_object(os.environ.get('APP_SETTINGS') or 'config')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'auth.login'
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from app.routes import bp as main_bp
app.register_blueprint(main_bp)
from app.routes import auth as auth_bp
app.register_blueprint(auth_bp, url_prefix='/auth')


db = SQLAlchemy()

from app.models import User

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
jwt = JWTManager()
from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

from app.models import User
@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)
    jwt.init_app(app)

    # Register blueprints
    from app.routes.products import products_bp
    from app.routes.cart import cart_bp
    from app.routes.orders import orders_bp
    from app.routes.auth import auth_bp
    from app.routes.vendors import vendors_bp
    from app.routes.transactions import transactions_bp

    app.register_blueprint(products_bp, url_prefix="/products")
    app.register_blueprint(cart_bp, url_prefix="/cart")
    app.register_blueprint(orders_bp, url_prefix="/orders")
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(vendors_bp, url_prefix="/vendors")
    app.register_blueprint(transactions_bp, url_prefix="/transactions")
from celery import Celery
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

    return app