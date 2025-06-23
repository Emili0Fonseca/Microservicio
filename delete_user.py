# delete_user.py

from flask import Flask, request, jsonify
from common.database import SessionLocal
from common.models import User

app = Flask(__name__)

@app.route("/delete", methods=["DELETE"])
def delete_user():
    # Obtener el parámetro 'id' de la solicitud
    user_id = request.args.get("id")

    # Validar que 'id' es proporcionado y es un número válido
    if not user_id or not user_id.isdigit():
        return jsonify({"error": " El parámetro 'id' es requerido y debe ser un numero válido"}), 400
    
    db = SessionLocal()
    
    # Buscar el usuario por 'id'
    user = db.query(User).filter(User.id == user_id).first()
    
    if user:
        # Eliminar el usuario
        db.delete(user)
        db.commit()
        db.close()
        return jsonify({"Mensaje": "Usuario eliminado"})
    
    # Cerrar la base de datos si el usuario no fue encontrado
    db.close()
    
    return jsonify({"error": "Usuario no encontrado"}), 404

if __name__ == "__main__":
    app.run(port=5004)
