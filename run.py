from app import create_app, db
from app.models import Product

import unittest

import sys

import os

from app import app

from app.models import TestModels

from app.routes.auth import TestAuthRoutes

from app.routes.cart import TestCartRoutes

from app.routes.orders import TestOrderRoutes

from app.routes.products import TestProductRoutes



if __name__ == '__main__':

    suite = unittest.TestSuite()

    suite.addTest(unittest.makeSuite(TestModels))

    suite.addTest(unittest.makeSuite(TestAuthRoutes))

    suite.addTest(unittest.makeSuite(TestCartRoutes))

    suite.addTest(unittest.makeSuite(TestOrderRoutes))

    suite.addTest(unittest.makeSuite(TestProductRoutes))

    runner = unittest.TextTestRunner()

    runner.run(suite)

from app import celery


@app.before_first_request
def seed_data():
    db.create_all()
    celery.start()
    if not Product.query.first():
        db.session.add_all([
            Product(name="T-shirt", price=20.0),
            Product(name="Sneakers", price=50.0),
            Product(name="Hat", price=15.0)
        ])
        db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)