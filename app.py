from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)

# Secret Key for session
app.secret_key = os.environ.get("SECRET_KEY", "mysecretkey")

# Temporary user storage
users = {}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        users[username] = password
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username] == password:
            session["user"] = username   # 🔐 login session set
            return redirect(url_for("tools"))
        else:
            return "Invalid username or password"

    return render_template("login.html")

@app.route("/tools")
def tools():
    if "user" not in session:   # 🔒 protect page
        return redirect(url_for("login"))
    return render_template("tools.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("home"))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)