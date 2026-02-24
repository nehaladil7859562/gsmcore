from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Secret Key for session management (from Environment Variable)
app.secret_key = os.environ.get("SECRET_KEY")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == "admin" and password == "1234":
            return redirect(url_for("tools"))
        else:
            return "<h3>Invalid credentials</h3><a href='/login'>Try again</a>"
    return render_template("login.html")

@app.route("/tools")
def tools():
    return render_template("tools.html")

if __name__ == "__main__":
    # Use Render's PORT environment variable, fallback to 10000 if not set
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
