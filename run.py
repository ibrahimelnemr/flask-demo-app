from app import create_app, db
from app.models import Product

app = create_app()

@app.before_first_request
def seed_data():
    db.create_all()
    if not Product.query.first():
        db.session.add_all([
            Product(name="T-shirt", price=20.0),
            Product(name="Sneakers", price=50.0),
            Product(name="Hat", price=15.0)
        ])
        db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)