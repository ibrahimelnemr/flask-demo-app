from flask import Blueprint, jsonify
from app.models import Transaction, Order, Vendor
from app import db
from flask_jwt_extended import jwt_required, get_jwt_identity

transactions_bp = Blueprint("transactions", __name__)

@transactions_bp.route("/", methods=["GET"])
@jwt_required()
def get_transactions():
    transactions = Transaction.query.all()
    return jsonify([
        {
            "id": t.id,
            "order_id": t.order_id,
            "vendor_id": t.vendor_id,
            "amount": t.amount
        } for t in transactions
    ])

@transactions_bp.route("/<int:order_id>", methods=["POST"])
@jwt_required()
def create_transaction(order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404

    vendor = Vendor.query.get(order.items[0].product.vendor_id)
    if not vendor:
        return jsonify({"error": "Vendor not found"}), 404

    transaction = Transaction(order_id=order_id, vendor_id=vendor.id, amount=order.total)
    db.session.add(transaction)
    db.session.commit()
    return jsonify({"message": "Transaction created", "id": transaction.id}), 201