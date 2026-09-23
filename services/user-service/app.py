from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "service": "user-service",
        "status": "running"
    })


@app.route("/users/<int:user_id>")
def get_user(user_id):
    users = {
        1: {
            "username": "admin",
            "email": "admin@example.com"
        },
        2: {
            "username": "student",
            "email": "student@example.com"
        },
        3: {
            "username": "developer",
            "email": "developer@example.com"
        }
    }

    user = users.get(user_id)

    if user:
        return jsonify(user)

    return jsonify({
        "message": "User not found"
    }), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)