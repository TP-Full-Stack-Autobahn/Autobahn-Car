from src import db
from dataclasses import dataclass


@dataclass
class Car(db.Model):
    __tablename__ = "cars"

    id: int
    name: str
    price: float
    image: str

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False)
    price = db.Column(db.Float, unique=False)
    image = db.Column(db.Text(), unique=False)

    def __init__(self, name, price, image):
        self.name = name
        self.price = price
        self.image = image
        
    def __repr__(self):
        return f'<Car {self.name}>'

    # Alternative without marshmallow-dataclass
    # def serialize(self):
    #     return {
    #         "id" : self.id,
    #         "name": self.name,
    #         "price": self.price,
    #         "image": self.image
    #     }