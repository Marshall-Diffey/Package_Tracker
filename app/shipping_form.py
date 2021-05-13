from flask import Flask
from flask_wtf import FlaskForm
from wtforms import (StringField, SelectField, BooleanField, SubmitField)
from wtforms.validators import DataRequired

from map.map import map

v = [DataRequired()]

class ShippingForm(FlaskForm):
    sender_name = StringField("Name of Sender", v)
    recipient_name = StringField("Name of Recipient", v)
    origin = SelectField("Origin", v, choices=map.keys())
    destination = SelectField("Destination", v)
    express_shipping = BooleanField(default=False)
    submit = SubmitField()