from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__) # Flask application instance

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY") # Database secret key parameter
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL") # Database URI parameter
db = SQLAlchemy(app) # SQLAlchemy instance

# Database model
class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    date = db.Column(db.Date)
    employment_status = db.Column(db.String(80))


@app.route("/", methods=["GET", "POST"])
def index():
    print(request.method)
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        date = request.form["date"]
        date_obj = datetime.strptime(date, "%Y-%m-%d") # Convert date string to date object
        employment_status = request.form["employment_status"]
        print(first_name, last_name, email, date, employment_status)

        # Create a new Form instance and add it to the database
        form = Form(first_name=first_name, last_name=last_name, email=email, date=date_obj, employment_status=employment_status)
        db.session.add(form)
        db.session.commit()

    return render_template("index.html")



if __name__ == "__main__":
    with app.app_context():
        db.create_all() # Creates database file in instance folder using Form class above
        app.run(debug=True, port=5000)