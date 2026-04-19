from flask import Flask, request, jsonify, render_template
from user_service import register_user

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    email = request.form.get("email")
    password = request.form.get("password")
    phone = request.form.get("phone")

    result = register_user(email, password, phone)

    return render_template("index.html", message=result)

if __name__ == "__main__":
    app.run(debug=True)