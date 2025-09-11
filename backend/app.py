from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api")
def home():
    return jsonify({"message": "Hello from Flask backend!"})

if __name__ == "__main__":
<<<<<<< HEAD
    app.run(host="0.0.0.0", port=8000)
=======
    app.run(host="0.0.0.0", port=8000)
>>>>>>> 9027baa7a88aaff63f4fc2a2d04faff5f972836f
