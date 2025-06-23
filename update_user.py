# update_user.py


from flask import Flask, request, jsonify
from common.database import SessionLocal
from common.models import User

app = Flask(__name__)

@app.route("/update", methods=["PUT"])
def update_user():
    # Verificar que el cuerpo de la solicitud contiene 'id'
    data = request.json
    if not data or not data.get("id"):
        return jsonify({"error": "El 'id' es requerido"}), 400

    db = SessionLocal()
    
    # Buscar el usuario por 'id'
    user = db.query(User).filter(User.id == data["id"]).first()
    
    if user:
        # Actualizar los campos con los nuevos valores
        user.name = data.get("name", user.name)
        user.email = data.get("email", user.email)
        
        # Confirmar cambios en la base de datos
        db.commit()
        db.refresh(user)
        
        db.close()
        
        return jsonify({
            "id": user.id,
            "name": user.name,
            "email": user.email
        })
    
    # Cerrar la base de datos si el usuario no fue encontrado
    db.close()
    
    return jsonify({"error": "Usuario no encontrado"}), 404

if __name__ == "__main__":
    app.run(port=5003)
