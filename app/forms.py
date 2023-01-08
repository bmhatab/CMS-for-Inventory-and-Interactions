from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateTimeField, SelectField,SubmitField,IntegerField
from wtforms.validators import DataRequired, Email

class CustomerForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone')
    address = StringField('Address')
    notes = TextAreaField('Notes')
    submit = SubmitField('Create Customer')


class InteractionForm(FlaskForm):
    interaction_type = SelectField('Interaction Type', validators=[DataRequired()], choices=[('phone', 'Phone Call'), ('email', 'Email'), ('meeting', 'In-Person Meeting'), ('chat', 'Chat'), ('social', 'Social Media')])
    interaction_date = DateTimeField('Interaction Date', validators=[DataRequired()], format='%Y-%m-%d %H:%M:%S')
    notes = TextAreaField('Notes')

class OrderForm(FlaskForm):
    customer_name = StringField('Name', validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    status = StringField('Price', validators=[DataRequired()])
    submit = SubmitField('Add product')