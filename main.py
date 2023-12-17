from flask import Flask, request, flash, url_for, redirect, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from model.Database import Fruit , Member , Supplier, Order , db
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:10350114@localhost/db_project'
app.config['SECRET_KEY'] = os.urandom(24)

db.init_app(app)
with app.app_context():
    db.create_all()

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/choose')
def choose():
    return render_template('choose.html')





#水果功能 顯示
@app.route('/fruit', methods=["GET"])
def gestFruit(): #顯示
    fruit = Fruit.query.all()
    return render_template('AboutFruit.html', fruits=fruit)

@app.route('/fruit', methods = ["POST"])
def newFruits(): #新增
    request_data = request.get_json()
    fruit = Fruit(request_data['ID'], request_data['F_name'], 
            request_data['Supplier'], request_data['Quantity'], 
            request_data['Unit'], request_data['Cost'], request_data['TotalValue']
            , request_data['PurchaseDate'], request_data['PromotionDate'])
    db.session.add(fruit)
    db.session.commit()
    return '', 204

#刪除
@app.route('/fruit/<ID>', methods = ["DELETE"])
def deleteFruit(ID):
    user = Fruit.query.filter_by(ID=ID).delete()
    db.session.commit()
    return '', 204

# @app.route('/fruit/<id>', methods = ["GET"])
# def getUser(id): #selection
#     fruit = Fruit.query.filter_by(id=id)
#     return jsonify(fruit[0])

# @app.route('/fruit', methods = ["DELETE"])
# def deleteUsers():
#     users = Fruit.query.delete()  
#     db.session.commit()
#     return '', 204

#####################################

#會員功能
@app.route('/member', methods=["GET"])
def getMembers():
    member = Member.query.all()
    return render_template('member.html', members=member)
#新增
@app.route('/member', methods = ["POST"])
def newMember():
    request_data = request.get_json()
    member = Member(request_data['MemberID'], request_data['Name'], request_data['Phone'], 
                    request_data['Mobile'], request_data['Email'], request_data['LineStatus'], 
                    request_data['Address'], request_data['Age'], request_data['Photo'], 
                    request_data['Discount'])
    db.session.add(member)
    db.session.commit()
    return '', 204
#刪除
@app.route('/member/<MemberID>', methods = ["DELETE"])
def deleteMember(MemberID):
    user = Member.query.filter_by(MemberID=MemberID).delete()
    db.session.commit()
    return '', 204


###############################

#供應商
@app.route('/supplier', methods=["GET"])
def getSuppliers():
    supplier = Supplier.query.all()
    return render_template('supplier.html', suppliers=supplier)
#新增
@app.route('/supplier', methods = ["POST"])
def newSupplier():
    request_data = request.get_json()
    supplier = Supplier(request_data['ID'], request_data['Name'], request_data['Phone'], request_data['Email'], request_data['Address'], request_data['Agent'])
    db.session.add(supplier)
    db.session.commit()
    return '', 204
#刪除
@app.route('/supplier/<ID>', methods = ["DELETE"])
def deleteSupplier(ID):
    user = Supplier.query.filter_by(ID=ID).delete()
    db.session.commit()
    return '', 204

######################################

#訂單
@app.route('/order', methods=["GET"])
def getOrders():
    order = Order.query.all()
    return render_template('order.html', orders=order)
#新增
@app.route('/order', methods = ["POST"])
def newOrder():
    request_data = request.get_json()
    order = Order(request_data['FruitID'],request_data['FruitName'],request_data['MemberID'],request_data['Quantity'],request_data['UnitPrice'],request_data['Total'],request_data['Discounted'],request_data['TransactionDate'],request_data['ExpectedDate'],request_data['ArrivedDate'])
    db.session.add(order)
    db.session.commit()
    return '', 204
#刪除
@app.route('/order/<MemberID>', methods = ["DELETE"])
def deleteOrder(MemberID):
    user = Order.query.filter_by(MemberID=MemberID).delete()
    db.session.commit()
    return '', 204
######################################
#修改
# @app.route('/member/<MemberID>', methods=["PUT"])
# def updateMember(MemberID):
#     print("hello")
#     member = Member.query.filter_by(MemberID=MemberID).first()

#     request_data = request.get_json()

#     # 更新會員資料
#     member.Name = request_data.get('Name', member.Name)
#     member.Phone = request_data.get('Phone', member.Phone)
#     member.Mobile = request_data.get('Mobile', member.Mobile)
#     member.Email = request_data.get('Email', member.Email)
#     member.LineStatus = request_data.get('LineStatus', member.LineStatus)
#     member.Address = request_data.get('Address', member.Address)
#     member.Age = request_data.get('Age', member.Age)
#     member.Photo = request_data.get('Photo', member.Photo)
#     member.Discount = request_data.get('Discount', member.Discount)

#     db.session.commit()

#查詢
# @app.route('/member/<id>', methods = ["GET"])
# def getMember(MemberID):
#     members = Member.query.filter_by(MemberID=MemberID)
#     return jsonify(members[0])


