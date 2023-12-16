from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
from datetime import date

db = SQLAlchemy()

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

    def __init__(self, ID, F_name, Supplier, Quantity, Unit, Cost, TotalValue,
                 Location, PurchaseDate, PromotionDate, Expiry):
        self.ID = ID
        self.F_name = F_name
        self.Supplier = Supplier
        self.Quantity = Quantity
        self.Unit = Unit
        self.Cost = Cost
        self.TotalValue = TotalValue
        self.Location = Location
        self.PurchaseDate = PurchaseDate
        self.PromotionDate = PromotionDate
        self.Expiry = Expiry

