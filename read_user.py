# read_user.py

from flask import Flask, request, jsonify
from common.database import SessionLocal
from common.models import User

app = Flask(__name__)

@app.route("/read", methods=["GET"])
def read_user():
    # Obtener el parámetro 'id' de la solicitud
    user_id = request.args.get("id")

    # Validar si 'id' es proporcionado y es un número válido
    if not user_id or not user_id.isdigit():
        return jsonify({"error": "Parámetro 'id' inválido"}), 400

    # Establecer la sesión de base de datos
    db = SessionLocal()
    
    # Consultar el usuario en la base de datos
    user = db.query(User).filter(User.id == user_id).first()
    
    # Cerrar la sesión
    db.close()

    # Si el usuario se encuentra, devolver los datos
    if user:
        return jsonify({
            "id": user.id,
            "name": user.name,
            "email": user.email
        })
    
    # Si el usuario no se encuentra, devolver error 404
    return jsonify({"error": "Usuario no encontrado"}), 404

if __name__ == "__main__":
    app.run(port=5002)
