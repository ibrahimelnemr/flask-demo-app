import unittest

//Add similar test structure as auth.py, adapting for cart routes and models
from flask import Blueprint, jsonify, request
from app.models import CartItem, Product, User
from app import db
from flask_jwt_extended import jwt_required, get_jwt_identity

cart_bp = Blueprint("cart", __name__)

@cart_bp.route("/", methods=["GET"])
@jwt_required()
def get_cart():
    user_id = get_jwt_identity()
    cart_items = CartItem.query.filter_by(user_id=user_id).all()
    return jsonify([
        {
            "id": item.id,
            "product_id": item.product_id,
            "name": item.product.name,
            "price": item.product.price,
            "quantity": item.quantity
        } for item in cart_items
    ])

@cart_bp.route("/", methods=["POST"])
@jwt_required()
def add_to_cart():
    user_id = get_jwt_identity()
    data = request.json
    product = Product.query.get(data["product_id"])
    if not product:
        return jsonify({"error": "Product not found"}), 404

    cart_item = CartItem(product_id=product.id, user_id=user_id, quantity=data.get("quantity", 1))
    db.session.add(cart_item)
    db.session.commit()
    return jsonify({"message": "Added to cart"}), 201