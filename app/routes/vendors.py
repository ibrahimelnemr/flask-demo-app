from flask import Blueprint, jsonify, request
from app.models import Vendor, VendorUser, Product
from app import db
from flask_jwt_extended import jwt_required, get_jwt_identity

vendors_bp = Blueprint("vendors", __name__)

@vendors_bp.route("/", methods=["GET"])
def get_vendors():
    vendors = Vendor.query.all()
    return jsonify([{"id": v.id, "name": v.name} for v in vendors])

@vendors_bp.route("/", methods=["POST"])
def add_vendor():
    data = request.json
    if Vendor.query.filter_by(name=data["name"]).first():
        return jsonify({"error": "Vendor already exists"}), 400

    vendor = Vendor(name=data["name"])
    db.session.add(vendor)
    db.session.commit()
    return jsonify({"message": "Vendor added", "id": vendor.id}), 201

@vendors_bp.route("/<int:vendor_id>/users", methods=["POST"])
def add_vendor_user(vendor_id):
    data = request.json
    vendor = Vendor.query.get(vendor_id)
    if not vendor:
        return jsonify({"error": "Vendor not found"}), 404

    if VendorUser.query.filter_by(username=data["username"]).first():
        return jsonify({"error": "Vendor user already exists"}), 400

    vendor_user = VendorUser(username=data["username"], vendor_id=vendor_id)
    vendor_user.set_password(data["password"])
    db.session.add(vendor_user)
    db.session.commit()
    return jsonify({"message": "Vendor user added", "id": vendor_user.id}), 201