from flask import Flask, jsonify
import os
app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "service": "product-service",
        "status": "running"
    })


@app.route("/products")
def products():
    products = [
        {
            "id": 1,
            "name": "Laptop",
            "price": 850
        },
        {
            "id": 2,
            "name": "Keyboard",
            "price": 45
        },
        {
            "id": 3,
            "name": "Mouse",
            "price": 25
        }
    ]

    return jsonify(products)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5003))
    app.run(host="0.0.0.0", port=port)
