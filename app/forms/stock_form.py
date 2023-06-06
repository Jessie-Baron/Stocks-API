from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField
from wtforms.validators import DataRequired, ValidationError

class StockForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    price = IntegerField("price", validators=[DataRequired()])
    price_change = IntegerField("price_change", validators=[DataRequired()])
    market_cap = IntegerField("market_cap", validators=[DataRequired()])
    revenue= IntegerField("revenue", validators=[DataRequired()])
    image= StringField("image", validators=[DataRequired()])
    date= DateField("date", validators=[DataRequired()])
