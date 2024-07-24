from flask import Flask, render_template, redirect

#---#---#---#---#---#---#---#---#---#---#---#---#


app = Flask(__name__)


#---#---#---#---#---#---#---#---#---#---#---#---#

@app.route("/")
def IndexPage():
    return render_template('index.html')

@app.route("/Introduction/")
def IntroductionPage():
    return render_template('HomePage.html')

#---#---#---#---#---#---#---#---#---#---#---#---#
