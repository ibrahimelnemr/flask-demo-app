from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()

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

    return app