from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
from datetime import date
from decimal import Decimal


db = SQLAlchemy()

#水果
@dataclass
class Fruit(db.Model):

    ID: str
    F_name: str
    Supplier: str
    Quantity: int
    Unit: str
    Cost: float
    TotalValue: float
    Location: str
    PurchaseDate: date
    PromotionDate: date
    Expiry: date

    ID = db.Column(db.String(16), primary_key=True)
    F_name = db.Column(db.String(16))
    Supplier = db.Column(db.String(16))
    Quantity = db.Column(db.Integer)
    Unit = db.Column(db.String(4))
    Cost = db.Column(db.Numeric(8, 2))
    TotalValue = db.Column(db.Numeric(8, 2))
    Location = db.Column(db.String(16))
    PurchaseDate = db.Column(db.Date)
    PromotionDate = db.Column(db.Date)
    Expiry = db.Column(db.Date)

    # def __init__(self, ID, F_name, Supplier, Quantity, Unit, Cost, TotalValue,
    #              Location, PurchaseDate, PromotionDate, Expiry):
    #     self.ID = ID
    #     self.F_name = F_name
    #     self.Supplier = Supplier
    #     self.Quantity = Quantity
    #     self.Unit = Unit
    #     self.Cost = Cost
    #     self.TotalValue = TotalValue
    #     self.Location = Location
    #     self.PurchaseDate = PurchaseDate
    #     self.PromotionDate = PromotionDate
    #     self.Expiry = Expiry

#會員
@dataclass
class Member(db.Model):

    MemberID: str
    Name: str
    Phone: str
    Mobile: str
    Email: str
    LineStatus: bool
    Address: str
    Age: int
    Photo: bytes
    Discount: Decimal

    MemberID = db.Column(db.String(12), primary_key=True)
    Name = db.Column(db.String(16))
    Phone = db.Column(db.String(20))
    Mobile = db.Column(db.String(20))
    Email = db.Column(db.String(50))
    LineStatus = db.Column(db.Boolean)
    Address = db.Column(db.String(60))
    Age = db.Column(db.Integer)
    Photo = db.Column(db.LargeBinary)
    Discount = db.Column(db.Numeric(3, 2))

    # def __init__(self, MemberID, Name, Phone, Mobile, Email, LineStatus, Address, Age, Photo, Discount):
    #     self.MemberID = MemberID
    #     self.Name = Name
    #     self.Phone = Phone
    #     self.Mobile = Mobile
    #     self.Email = Email
    #     self.LineStatus = LineStatus
    #     self.Address = Address
    #     self.Age = Age
    #     self.Photo = Photo
    #     self.Discount = Discount


