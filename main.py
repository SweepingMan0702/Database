from flask import Flask, request, flash, url_for, redirect, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from model.Fruit import Fruit, db
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:10350114@localhost/db_project'
app.config['SECRET_KEY'] = os.urandom(24)

@app.route('/')
def login_page():
    return render_template('login.html')


db.init_app(app)
with app.app_context():
    db.create_all()



@app.route('/fruit', methods=["GET"])
def getUsers():
    fruit = Fruit.query.all()
    return render_template('fruit.html', fruits=fruit)

@app.route('/fruit', methods = ["POST"])
def newUsers():
    request_data = request.get_json()
    fruit = Fruit(request_data['username'], request_data['password'])
    db.session.add(fruit)
    db.session.commit()
    return '', 204

@app.route('/fruit/<id>', methods = ["GET"])
def getUser(id):
    fruit = Fruit.query.filter_by(id=id)
    return jsonify(fruit[0])

@app.route('/fruit', methods = ["DELETE"])
def deleteUsers():
    users = Fruit.query.delete()  
    db.session.commit()
    return '', 204

@app.route('/fruit/<id>', methods = ["DELETE"])
def deleteUser(id):
    user = Fruit.query.filter_by(id=id).delete()
    db.session.commit()
    return '', 204