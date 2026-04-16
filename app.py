from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = "gsmcore_secret_key"

users = {}

@app.route("/")
def home():
    return redirect(url_for("login"))

# LOGIN
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username]["password"] == password:
            session["user"] = username
            return redirect(url_for("dashboard"))
        else:
            return "Invalid username or password"

    return render_template("login.html")


# REGISTER STEP 1
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        phone = request.form["phone"]
        location = request.form["location"]

        if username in users:
            return "User already exists"

        # OTP generate
        otp = str(random.randint(1000, 9999))
        print("OTP:", otp)  # 👈 console mein show hoga

        # temp data save
        session["temp_user"] = {
            "username": username,
            "password": password,
            "phone": phone,
            "location": location,
            "otp": otp
        }

        return redirect(url_for("verify_otp"))

    return render_template("register.html")


# OTP VERIFY
@app.route("/verify", methods=["GET", "POST"])
def verify_otp():
    if "temp_user" not in session:
        return redirect(url_for("register"))

    if request.method == "POST":
        user_otp = request.form["otp"]
        real_otp = session["temp_user"]["otp"]

        if user_otp == real_otp:
            data = session["temp_user"]

            users[data["username"]] = {
                "password": data["password"],
                "phone": data["phone"],
                "location": data["location"]
            }

            session.pop("temp_user", None)
            return redirect(url_for("login"))
        else:
            return "Invalid OTP"

    return render_template("verify.html")


# DASHBOARD
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))

    user = session["user"]
    data = users[user]

    return render_template("dashboard.html", user=user, data=data)


# LOGOUT
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)