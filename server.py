from flask import Flask, request, redirect
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'fandom_pokemon_db')

@app.route("/")
def index():
    return "Hello World!"

@app.route("/allusers")
def getAllUsers():
    query = "SELECT * FROM users"
    allUsers = mysql.query_db('SELECT * FROM users')
    print(allUsers)
    return redirect("/")

@app.route("/register", methods=['POST'])
def register():
    query = 'INSERT INTO users (email, username, password, created_at, updated_at) VALUES (:email, :username, :password, NOW(), NOW())'
    data = {
        'email': request.form['email'],
        'username': request.form['username'],
        'password': request.form['password']
    }
    mysql.query_db(query, data)
    return redirect("/")
app.run(debug=True)