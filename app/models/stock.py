from .db import db, environment, SCHEMA, add_prefix_for_prod

class Stock(db.Model):
    __tablename__ = 'stocks'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
    price_change = db.Column(db.Integer, nullable=False)
    market_cap = db.Column(db.Integer, nullable=False)
    revenue = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(40), nullable=False, unique=True)
    date= db.Column(db.String)

    



    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'price change': self.price_change,
            'market cap': self.market_cap,
            'revenue': self.revenue,
            'image': self.image,
            'date': self.date  
        }