import os
import uuid0
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = "FGAWP"

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        json_data = request.json
        isGoogleProvider = json_data["isGoogleProvider"]
        if(isGoogleProvider):
            token = json_data["token"]
            session['token'] = token
        else:
            session['token'] = uuid0.generate()
        return redirect("/profile")
    
@app.route('/profile')
def profile():
    if 'token' in session:
        return render_template('profile.html')
    else:
        return redirect("/")


@app.route("/signOut")
def signOut():
    if 'token' in session:
        session.pop('token', None)
        return redirect("/")
if __name__ == "__main__":
    app.run(host="localhost")