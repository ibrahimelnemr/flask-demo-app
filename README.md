# 🛍️ Comprehensive Flask eCommerce API

This is a **comprehensive Python Flask backend** for an eCommerce platform. It includes features for managing users, vendors, products, carts, orders, and transactions.

---

## 🛠️ Features

- **User Authentication**:
  - Register and login with JWT-based authentication.
- **Product Management**:
  - List and add products.
- **Cart Management**:
  - Add products to a user-specific cart.
  - View the cart.
- **Order Management**:
  - Place orders from the cart.
- **Vendor Management**:
  - Add vendors and vendor users.
  - Associate products with vendors.
- **Transaction Management**:
  - Create and view transactions associated with orders and vendors.

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/flask-ecommerce-sample.git
cd flask-ecommerce-sample
```

### 2. (Optional) Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Run the Application

python app.py

The API will start at http://localhost:5000.

---

## 🐳 Running with Docker

### Build the Docker image

docker build -t flask-ecommerce .

### Run the Docker container

docker run -p 5000:5000 flask-ecommerce

Now visit http://localhost:5000.

---

## ✅ Requirements

- Python 3.7+
- Flask

---

## 📁 File Structure

.
├── app.py
├── requirements.txt
└── README.md

---

## 🧪 Use Cases

This repository is useful for:
- Testing AI tools that analyze or suggest backend code changes
- Simple API testing with Postman or curl
- Teaching basic API concepts with Flask

---

## 📖 License

This project is open-source and available under the MIT License.
