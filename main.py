from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import smtplib

my_email = "forpython574450@gmail.com"
password = "gihphbjnqmjioomb"



app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        print(data["name"])
        print(data["email"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

@app.route("/projects")
def projects():
    return render_template("projects.html")


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="shegedarharsh@gmail.com", msg=email_message)




if __name__ == '__main__':
    app.run(debug=True)