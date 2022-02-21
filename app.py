from flask import Flask, render_template, request
from model import *

app = Flask(__name__)
products = []
price = 0


@app.route('/')
def home():
    global products
    global price
    products = []
    price = 0
    result = session.query(Events, Fee).filter(Events.fee_id == Fee.id).all()
    return render_template('index.html', data=result)


@app.route('/submit_event', methods=["POST"])
def submit_event():
    global products
    global price
    products = []
    price = 0

    name = request.form['event']
    event = session.query(Events).filter(Events.name == name).first()
    eventProduct = session.query(EventProduct).filter(event.id == EventProduct.event_id).all()
    fee = session.query(Fee).filter(Fee.id == event.fee_id).first()
    price = fee.value

    for e in eventProduct:
        p = session.query(Products).filter(Products.id == e.product_id).first()
        result = session.query(Products, Fee).filter(p.fee_id == Fee.id).filter(Products.id == p.id).first()
        products.append(result)

    return render_template('products.html', data=products, fee=price)


@app.route('/submit_products', methods=["POST"])
def submit_products():
    global price
    result = float(request.form.get('price'))
    price += result
    return render_template('products.html', data=products, fee=price)


if __name__ == '__main__':

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    app.run()
