from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api")
def home():
    return jsonify({"message": "Hello from Flask backend!"})

if __name__ == "_main_":
    app.run(host="0.0.0.0", port=5000)