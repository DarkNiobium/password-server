import os
from flask import Flask, jsonify

app = Flask(__name__)

PASSWORD = os.environ.get("PASSWORD", "1234")

@app.route("/get_password")
def get_password():
    return jsonify({"password": PASSWORD})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
