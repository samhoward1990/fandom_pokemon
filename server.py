from flask import Flask, request, redirect
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'fandom_pokemon_db_test')

@app.route("/")
def index():
    return "Hello World!"

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
    query = 'INSERT INTO users (email, username, password, created_at, updated_at) VALUES (:email, :username, :password, NOW(), NOW())'
    data = {
        'email': request.form['email'],
        'username': request.form['username'],
        'password': request.form['password']
    }
    newUser = mysql.query_db(query, data)
    return newUser

@app.route('/createcharacter', methods=['POST'])
def createCharacter():
    query = 'INSERT INTO characters (name, created_at, updated_at) VALUES (:name, NOW(), NOW())'
    data = {
        'name': request.form['name'],
        'fandom': request.form['fandom']
    }
    mysql.query_db(query, data)
    return redirect('/')
app.run(debug=True)