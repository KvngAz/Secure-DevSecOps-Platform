from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

DATABASE = "users.db"


def get_db():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    connection = get_db()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    connection.execute("""
        INSERT OR IGNORE INTO users (username, password)
        VALUES ('admin', 'admin123')
    """)

    connection.commit()
    connection.close()


@app.route("/")
def home():
    return jsonify({
        "service": "auth-service",
        "status": "running"
    })


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    # Intentionally vulnerable SQL query.
    # This vulnerability exists only for our controlled security lab.
    query = f"""
        SELECT id, username
        FROM users
        WHERE username = '{username}'
        AND password = '{password}'
    """

    connection = get_db()
    user = connection.execute(query).fetchone()
    connection.close()

    if user:
        return jsonify({
            "message": "Login successful",
            "user_id": user["id"],
            "username": user["username"]
        })

    return jsonify({
        "message": "Invalid username or password"
    }), 401


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5001, debug=False)