from flask import Flask, render_template, redirect

#---#---#---#---#---#---#---#---#---#---#---#---#


app = Flask(__name__)


#---#---#---#---#---#---#---#---#---#---#---#---#

@app.route("/HomePage/")
def HomePage():
    return render_template('HomePage.html')

#---#---#---#---#---#---#---#---#---#---#---#---#
