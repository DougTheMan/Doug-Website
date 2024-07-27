from app import app
from flask import render_template, redirect

@app.route("/")
#login required
def index():
    return render_template('HomePage.html')

@app.route("/homepage/")
def HomePage():
    return render_template('HomePage.html')

@app.route("/portifolio/")
def PortPage():
    return render_template('PortPage.html')

@app.route("/contacting/")
def ContactPage():
    return render_template('ContactPage.html')