from flask import Flask, request, redirect
from mysqlconnection import MySQLConnection
app = Flask(__name__)
mysql = MySQLConnection.MySQLConnector(app, 'fandom_Pokemon_db')

@app.route("/")
def index():
    return "Hello World!"

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