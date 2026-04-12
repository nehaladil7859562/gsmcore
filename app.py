import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home Page
@app.route("/")
def home():
    return render_template("home.html")

# Login Page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Simple check (you can upgrade later)
        if username == "admin" and password == "1234":
            return redirect(url_for("home"))
        else:
            return "Invalid Credentials ❌"

    return render_template("login.html")

# Register Page
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        return redirect(url_for("login"))

    return render_template("register.html")

# IMPORTANT: Railway Deployment Fix
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)