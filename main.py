from flask import Flask, request, flash, url_for, redirect, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from model.Database import Fruit , Member , Supplier , db
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:10350114@localhost/db_project'
app.config['SECRET_KEY'] = os.urandom(24)

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/choose')
def choose():
    return render_template('choose.html')




db.init_app(app)
with app.app_context():
    db.create_all()



#水果功能 顯示
@app.route('/fruit', methods=["GET"])
def gestUser(): #顯示
    fruit = Fruit.query.all()
    return render_template('AboutFruit.html', fruits=fruit)

@app.route('/fruit', methods = ["POST"])
def newUsers(): #新增
    request_data = request.get_json()
    fruit = Fruit(request_data['ID'], request_data['F_name'], request_data['Supplier'], request_data['Quantity'], request_data['Unit'], request_data['Cost'], request_data['TotalValue'], request_data['Location'], request_data['PurchaseDate'], request_data['PromotionDate'],request_data['Expiry'])
    db.session.add(fruit)
    db.session.commit()
    return '', 204

#刪除
@app.route('/fruit/<ID>', methods = ["DELETE"])
def deleteFruit(ID):
    print("刪除",ID) 
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
    member = Member(request_data['MemberID'], request_data['Name'], request_data['Phone'], request_data['Mobile'], request_data['Email'], request_data['LineStatus'], request_data['Address'], request_data['Age'], request_data['Photo'], request_data['Discount'])
    db.session.add(member)
    db.session.commit()
    return '', 204
#刪除
@app.route('/member/<MemberID>', methods = ["DELETE"])
def deleteMember(MemberID):
    print("刪除",MemberID) 
    user = Member.query.filter_by(MemberID=MemberID).delete()
    db.session.commit()
    return '', 204


###############################

#供應商
@app.route('/supplier', methods=["GET"])
def getSuppliers():
    supplier = Supplier.query.all()
    print(supplier)
    return render_template('supplier.html', suppliers=supplier)
#新增
@app.route('/supplier', methods = ["POST"])
def newSupplier():
    request_data = request.get_json()
    supplier = Supplier(request_data['MemberID'], request_data['Name'], request_data['Phone'], request_data['Mobile'], request_data['Email'], request_data['LineStatus'], request_data['Address'], request_data['Age'], request_data['Photo'], request_data['Discount'])
    db.session.add(supplier)
    db.session.commit()
    return '', 204
#刪除
@app.route('/supplier/<ID>', methods = ["DELETE"])
def deleteSupplier(ID):
    print("刪除",ID) 
    user = Supplier.query.filter_by(ID=ID).delete()
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


