#!/usr/bin/env python

from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext import restless

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
# Create the Flask-Restless API manager.
manager = restless.APIManager(app, flask_sqlalchemy_db=db)

class User(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, primary_key=True)
    email = db.Column(db.String(120), unique=True)

    def __repr__(self):
        return '<User %r>' % self.username

# Create API endpoints, which will be available at /api/<tablename> by
# default. Allowed HTTP methods can be specified as well.
manager.create_api(User, methods=['GET', 'POST', 'PUT', 'DELETE'])

# tested with these curl commands: (when the primary key was id)
# curl http://localhost:5000/api/user
# curl -X POST -H "Content-Type: application/json" -d '{"username":"bob","email":"bob@bobstractors.com"}' http://localhost:5000/api/user
# curl -X PUT -H "Content-Type: application/json" -d '{"email":"bob@bobstractorsandtrucks.com"}' http://localhost:5000/api/user/3
# curl -X DELETE  http://localhost:5000/api/user/3

@app.route("/")
def index():
    # TODO: Add a front page template, or just make the main page an insult
    return "The Shakespeare Insult Generator."

@app.route("/insult/<name>")
def insult_someone(name):
    return render_insult(name)

@app.route('/insult/')
def hello():
    return render_insult(None)

def render_insult(name):
    adj1 = 'APISH'
    adj2 = 'BALD-PATED'
    noun = 'ABOMINATION'
    response =  render_template('insult.html', name=name, adj1=adj1, adj2=adj2, noun=noun)
    return response

if __name__ == "__main__":
    app.debug = True
    app.run()
