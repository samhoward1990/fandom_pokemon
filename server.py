from flask import Flask, request, redirect
from mysqlconnection import MySQLConnector
import hashlib
import os, binascii
app = Flask(__name__)
mysql = MySQLConnector(app, 'fandom_pokemon')

@app.route("/")
def index():
    return "Hello World!"

@app.route("/testdata")
def get_test_data():
    return {
        "name": "Pikachu",
        "type": "Electric",
        "hp": 35,
        "attack": 55,
        "defense": 40,
    }

@app.route("/allusers")
def getAllUsers():
    query = "SELECT * FROM users"
    allUsers = mysql.query_db('SELECT * FROM users')
    print(allUsers)
    users = {}
    for user in allUsers:
        users[user['email']] = user
    return users

@app.route("/register", methods=['POST'])
def register():
    email = request.form['email']
    userName = request.form['username']
    password = request.form['password']
    print(password)
    salt = binascii.b2a_hex(os.urandom(15))
    hashedPW = hashlib.md5("{}{}".format(password, salt).encode()).hexdigest()
    print(hashlib.md5("{}{}".format("12345678", salt).encode()).hexdigest())
    print(hashlib.md5("{}{}".format("12345678", salt).encode()).hexdigest())
    query = 'INSERT INTO users (email, username, password, salt, created_at, updated_at) VALUES (:email, :username, :password, :salt, NOW(), NOW())'
    data = {
        'email': email,
        'username': userName,
        'password': hashedPW,
        'salt': salt
    }
    mysql.query_db(query, data)
    return redirect('/')
    
@app.route("/login", methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    print(password)
    query = "SELECT * FROM users WHERE users.email = :email LIMIT 1"
    data = {
        "email": email
    }
    user = mysql.query_db(query, data)
    print(user[0])
    print(user[0]['password'])
    if len(user) != 0:
        encryptedPW = hashlib.md5(f"{password}{user[0]['salt']}".encode()).hexdigest()
        print(hashlib.md5("remember{}".format(user[0]['salt']).encode()).hexdigest())
        print(hashlib.md5("remember{}".format(user[0]['salt']).encode()).hexdigest())
        print(encryptedPW)
        print(user[0]['salt'])
        print(user[0]['password'])
        if encryptedPW == user[0]['password']:
            return f"{user[0]['id']}"
        return "Invalid Password!"
    return "Invalid Email!"

@app.route('/createcharacter', methods=['POST'])
def createCharacter():
    query = 'INSERT INTO characters (name, created_at, updated_at) VALUES (:name, NOW(), NOW())'
    data = {
        'name': request.form['name'],
        'fandom': request.form['fandom']
    }
    mysql.query_db(query, data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
