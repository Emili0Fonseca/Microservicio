# create_user.py

from flask import Flask, request, jsonify
from common.database import SessionLocal, engine
from common.models import User, Base

app = Flask(__name__)

# Crear las tablas si no existen
Base.metadata.create_all(bind=engine)

@app.route("/create", methods=["POST"])
def create_user():
    global db
    try:
        data = request.json

        # Validación básica
        if not data or not data.get("name") or not data.get("email"):
            return jsonify({"error": "Faltan campos requeridos: 'name' y 'email'"}), 400

        db = SessionLocal()
        new_user = User(name=data["name"], email=data["email"])
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        response = {
            "id": new_user.id,
            "name": new_user.name,
            "email": new_user.email
        }
        return jsonify(response), 201

    except Exception as e:
        print("ERROR al crear usuario:", e)
        return jsonify({"error": str(e)}), 500

    finally:
        db.close()

if __name__ == "__main__":
    app.run(port=5001)
