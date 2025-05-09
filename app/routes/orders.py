import unittest

//Add similar test structure as auth.py, adapting for order routes and models
from flask import Blueprint, jsonify
from app.models import CartItem, Order
from app import db
from flask_jwt_extended import jwt_required, get_jwt_identity

orders_bp = Blueprint("orders", __name__)

@orders_bp.route("/", methods=["POST"])
@jwt_required()
def place_order():
    user_id = get_jwt_identity()
    cart_items = CartItem.query.filter_by(user_id=user_id).all()
    if not cart_items:
        return jsonify({"error": "Cart is empty"}), 400

    total = sum(item.product.price * item.quantity for item in cart_items)
    order = Order(user_id=user_id, total=total)
    db.session.add(order)

    for item in cart_items:
        db.session.delete(item)

    db.session.commit()
    return jsonify({"message": "Order placed", "total": total}), 201