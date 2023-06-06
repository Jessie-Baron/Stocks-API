from app.models import Stock, db
from flask import Blueprint, request, jsonify
from app.forms import StockForm


stock_routes = Blueprint('stock', __name__)

def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f'{error}')
    return errorMessages

@stock_routes.route('')
def get_stock():
    data = Stock.query.all()
    print("this is the data", data)
    return {stock.to_dict()['id']: stock.to_dict() for stock in data}

@stock_routes.route('/<int:id>')
def get_stock_id(id):
    data = Stock.query.get(id)
    return data.to_dict()

@stock_routes.route('', methods=['POST'])
def stock_purchase(id):
    form = StockForm()
    if form.validate_on_submit():
        stock_upload = Stock(
                    name = form.data['name'],
                    price = form.data['price'],
                    price_change = form.data['price change'],
                    market_cap = form.data['market cap'],
                    revenue = form.data['revenue'],
                    image = form.data['image'],
                    date = form.data['date'],
                    id = id.id 
        )
        db.session.add(stock_upload)
        db.session.commit()
        return stock_upload.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401
pass


@stock_routes.route('/<int:id>', methods=['PUT'])
def edit_stock(id):
    stock = Stock.query.get(id)
    if id.id == stock.id: 
        form = StockForm()
        if form.validate_on_submit():
            stock.name = form.data['name'], 
            stock.price = form.data['price'], 
            stock.price_change = form.data['price change'], 
            stock.market_cap = form.data['market cap'],
            stock.revenue = form.data['revenue'],
            stock.image = form.data['image'],
            stock.date = form.data['date'],
            db.session.add(stock)  
            db.session.commit()
            return stock.to_dict()
        return {'errors': validation_errors_to_error_messages(form.errors)}, 401
    return {'errors': ['Unauthorized']}
pass

@stock_routes.route('/<int:id>', methods=['DELETE'])
def delete_stock(id):
    stock = Stock.query.get(id)
    if id.id == stock.id:
        db.session.delete(stock)
        db.session.commit()
        return {"data": "Deleted"}
    return {'errors': ['Unauthorized']}
pass
        
