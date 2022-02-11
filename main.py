from flask import Flask, redirect
import bcrypt

password = b"SecretPassword94"

hashed = bcrypt.hashpw(password, bcrypt.gensalt())

username = request.form.get("username")
password = request.form.get("password").encode("utf-8")

if bcrypt.checkpw(password, hashed):
    print("welcome")
    redirect(url_for("user_profile"))
else:
    print("wrong pw")
    flash("No match")


app = Flask(__name__)

@app.route("/")
def helloWorld():
    return "Hello World!"

app.run(debug=True)