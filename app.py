from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

<<<<<<< HEAD
# Secret Key for session management (from Environment Variable)
app.secret_key = os.environ.get("SECRET_KEY")
=======
# Temporary user storage (basic version)
users = {}
>>>>>>> 0a587a3 (Updated home.html with new welcome + tagline)

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
            return redirect(url_for("tools"))
        else:
            return "Invalid username or password"

    return render_template("login.html")

@app.route("/tools")
def tools():
    return render_template("tools.html")

if __name__ == "__main__":
<<<<<<< HEAD
    # Use Render's PORT environment variable, fallback to 10000 if not set
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
=======
    app.run(port=10000, debug=True)
>>>>>>> 0a587a3 (Updated home.html with new welcome + tagline)
