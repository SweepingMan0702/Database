from flask import Flask, request, flash, url_for, redirect, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from model.users import Users, db
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:10350114@localhost/test'
app.config['SECRET_KEY'] = os.urandom(24)

db.init_app(app)
with app.app_context():
    db.create_all()

@app.route('/user', methods=["GET"])
def getUsers():
    users = Users.query.all()
    return render_template('index.html', users=users)

@app.route('/user', methods = ["POST"])
def newUsers():
    request_data = request.get_json()
    user = Users(request_data['username'], request_data['password'])
    db.session.add(user)
    db.session.commit()
    return '', 204

@app.route('/user/<id>', methods = ["GET"])
def getUser(id):
    user = Users.query.filter_by(id=id)
    return jsonify(user[0])

@app.route('/user', methods = ["DELETE"])
def deleteUsers():
    users = Users.query.delete()  
    db.session.commit()
    return '', 204

@app.route('/user/<id>', methods = ["DELETE"])
def deleteUser(id):
    user = Users.query.filter_by(id=id).delete()
    db.session.commit()
    return '', 204