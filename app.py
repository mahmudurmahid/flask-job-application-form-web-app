from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    print(request.method)
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        date = request.form["date"]
        employment_status = request.form["employment_status"]
        print(first_name, last_name, email, date, employment_status)

    return render_template("index.html")




app.run(debug=True, port=5000)