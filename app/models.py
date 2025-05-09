import unittest

from app.models import Product, User, Order, CartItem # Assuming these are your models



class TestModels(unittest.TestCase):

    def test_product_creation(self):

        product = Product(name='Test Product', price=10.99)

        self.assertEqual(product.name, 'Test Product')

        self.assertEqual(product.price, 10.99)

    # Add more tests for other model methods and attributes



if __name__ == '__main__':

    unittest.main()

from app import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)
    quantity = db.Column(db.Integer, default=1)
    product = db.relationship("Product", backref="cart_items")

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    total = db.Column(db.Float, nullable=False)
    items = db.relationship("CartItem", backref="order", lazy=True)