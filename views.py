from flask import Blueprint, render_template

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("home.html")

@views.route("/stocks")
def stocks():
    return "stocks"

@views.route("/companies")
def companies():
    return "companies"

@views.route("/sector")
def sector():
    return "sector"