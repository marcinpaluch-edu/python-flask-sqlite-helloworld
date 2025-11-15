from flask import jsonify
from app import create_app

# Create the app using the factory
app = create_app("development")

# Root route returns JSON for consistency
@app.route("/")
def index():
    return jsonify({
        "message": "Flask app is running 🚀",
        "endpoints": [
            "/users/hello",
            "/users/ (GET - list users, POST - create user)"
        ]
    })

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)