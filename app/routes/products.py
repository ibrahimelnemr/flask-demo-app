import unittest

//Add similar test structure as auth.py, adapting for product routes and models
from flask import Blueprint, jsonify, request
from app.models import Product
from app import db

products_bp = Blueprint("products", __name__)

@products_bp.route("/", methods=["GET"])
def get_products():
    products = Product.query.all()
    return jsonify([{"id": p.id, "name": p.name, "price": p.price} for p in products])

@products_bp.route("/", methods=["POST"])
def add_product():
    data = request.json
    new_product = Product(name=data["name"], price=data["price"])
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"message": "Product added", "id": new_product.id}), 201