from flask import Flask
from flask import (abort,render_template,request,redirect,url_for,flash,current_app,jsonify)
app = Flask(__name__)

@app.route('/<string:page_name>/')

def index(page_name):
    return render_template('%s.html' % page_name) 

if __name__ == '__main__':
    app.run()
