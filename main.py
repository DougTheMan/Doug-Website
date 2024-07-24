from flask import Flask, render_template, redirect

#---#---#---#---#---#---#---#---#---#---#---#---#


app = Flask(__name__)


#---#---#---#---#---#---#---#---#---#---#---#---#

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/HomePage/")
def HomePage():
    return render_template('HomePage.html')

#---#---#---#---#---#---#---#---#---#---#---#---#
