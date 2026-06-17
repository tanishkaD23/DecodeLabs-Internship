from flask import Flask, render_template, request
from randompassG import generate_password

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    password = ""

    if request.method == "POST":

        length = request.form.get("length")

        if length:

            length = int(length)

            password = generate_password(length)

    return render_template(
        "index.html",
        password=password
    )

if __name__ == "__main__":
    app.run(debug=True)