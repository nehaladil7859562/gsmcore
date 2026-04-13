import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for
from database import create_db

app = Flask(__name__)

create_db()

@app.route("/")
def home():
    return render_template("home.html")

# REGISTER
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")
        phone = request.form.get("phone")
        location = request.form.get("location")

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO users (username, password, email, phone, location) VALUES (?, ?, ?, ?, ?)",
            (username, password, email, phone, location)
        )

        conn.commit()
        conn.close()

        return redirect(url_for("login"))

    return render_template("register.html")

# LOGIN
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()

        conn.close()

        if user:
            return redirect(url_for("home"))
        else:
            return render_template("login.html", error="Invalid username or password ❌")

    return render_template("login.html")

# RUN
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)