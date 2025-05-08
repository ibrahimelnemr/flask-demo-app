from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock data
products = [
    {"id": 1, "name": "T-shirt", "price": 20.0},
    {"id": 2, "name": "Sneakers", "price": 50.0},
    {"id": 3, "name": "Hat", "price": 15.0},
]

cart = []

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)

@app.route("/cart", methods=["GET", "POST"])
def manage_cart():
    if request.method == "POST":
        data = request.json
        product_id = data.get("product_id")
        quantity = data.get("quantity", 1)

        product = next((p for p in products if p["id"] == product_id), None)
        if not product:
            return jsonify({"error": "Product not found"}), 404

        cart.append({
            "product_id": product["id"],
            "name": product["name"],
            "price": product["price"],
            "quantity": quantity
        })
        return jsonify({"message": "Added to cart"}), 201

    return jsonify(cart)

@app.route("/order", methods=["POST"])
def place_order():
    if not cart:
        return jsonify({"error": "Cart is empty"}), 400

    total = sum(item["price"] * item["quantity"] for item in cart)
    order = {
        "items": cart.copy(),
        "total": total
    }
    cart.clear()
    return jsonify(order)

if __name__ == "__main__":
    app.run(debug=True)
