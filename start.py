from flask import Flask
from flask import (abort,render_template,request,redirect,url_for,flash,current_app,jsonify)
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html') 

if __name__ == '__main__':
    app.run()
