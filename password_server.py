import os
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Значения будут подставлены через переменные окружения на Render
PASSWORD = os.environ.get("PASSWORD", "changeme")
SECRET_TOKEN = os.environ.get("SECRET_TOKEN", "devtoken")

@app.route("/get_password", methods=["GET"])
def get_password():
    # Проверяем заголовок Authorization: Bearer <token>
    auth = request.headers.get("Authorization", "")
    if not auth.startswith("Bearer "):
        abort(401)
    token = auth.split(" ", 1)[1].strip()
    if token != SECRET_TOKEN:
        abort(403)
    return jsonify({"password": PASSWORD})

if __name__ == "__main__":
    # Для локальной отладки: берем порт из переменных (Render передаёт $PORT)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
