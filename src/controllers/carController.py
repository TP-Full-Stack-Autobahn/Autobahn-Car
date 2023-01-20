from flask import Flask, request, jsonify
import json
from src import app, db
from src.models.carModel import Car


@app.route("/", methods=["GET"])
def hello():
    return jsonify({"Hello":"World"}), 200


@app.route('/cars')
def index():
    cars = Car.query.all()
    return jsonify(cars=[Car.serialize(car) for car in cars]), 200

@app.route('/cars/create', methods=['POST'])
def add_car():
    data = json.loads(request.data)
    name = data['name']
    price = data['price']
    image = data['image']

    car = Car(name=name, price=price, image=image)
    db.session.add(car)
    db.session.commit()

    return jsonify({"message": "Entity successfully added"}), 201


@app.route('/cars/edit/<int:id>', methods=['PUT'])
def edit_car(id):
    car = Car.query.get(id)
    car.name = request.form['name']
    car.price = request.form['price']
    car.image = request.form['image']

    db.session.commit()
    return jsonify({"message": "Entity successfully updated"}), 200


@app.route('/cars/delete/<int:id>', methods=['DELETE'])
def delete_car(id):
    car = Car.query.get(id)
    db.session.delete(car)
    db.session.commit()
    return jsonify({"message": "Entity successfully removed"}), 200
