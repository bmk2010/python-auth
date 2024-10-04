from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['JWT_SECRET_KEY'] = 'movie_app'
jwt = JWTManager(app)

# Foydalanuvchi loginlari va parollari
users = {
    "user1": "password1",
    "user2": "password2"
}

# Foydalanuvchilarni ko'rsatish
@app.route('/users', methods=["GET"])
def showUsers():
    return jsonify(users), 200

# Login orqali autentifikatsiya qilish
@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Iltimos, JSON formatida ma'lumot yuboring"}), 400

    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"msg": "Username va parol kiriting"}), 400
    
    # Foydalanuvchi mavjudligini va parolni tekshirish
    if username in users and users[username] == password:
        token = create_access_token(identity=username)
        return jsonify(access_token=token), 200
    else:
        return jsonify({"msg": "Noto'g'ri username yoki parol"}), 401

# Ilovani ishga tushirish
if __name__ == '__main__':
    app.run(debug=True)  # debug rejimini mahalliy muhitda faollashtiring
