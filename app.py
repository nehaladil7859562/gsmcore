from flask import Flask, render_template, request, redirect, session
from database import create_table, add_user, check_user

app = Flask(__name__)
app.secret_key = "gsmcore_secret_key"

# 🧠 Create database table on startup
create_table()


# ---------------- HOME ----------------
@app.route("/")
def home():
    return render_template("home.html")


# ---------------- REGISTER ----------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        try:
            add_user(username, password)
            return redirect("/login")
        except:
            return "User already exists!"

    return render_template("register.html")


# ---------------- LOGIN ----------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = check_user(username, password)

        if user:
            session["user"] = username
            return redirect("/tools")   # dashboard
        else:
            return "Invalid username or password"

    return render_template("login.html")


# ---------------- TOOLS (DASHBOARD) ----------------
@app.route("/tools")
def tools():
    if "user" in session:
        return render_template("tools.html", user=session["user"])
    else:
        return redirect("/login")


# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")


# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run(debug=True)