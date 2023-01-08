from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash



class Users(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200),nullable=False)
    email = db.Column(db.String(120),nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    # password work stuff
    password_hash = db.Column(db.String(128))
    

    @property
    def password(self):
        raise AttributeError('Password does not have a read attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash

    def verify_password(self,password):
        return check_password_hash(self.password_hash, password)


    # Create a string
    def __repr__(self):
        return '<Name %r>' % self.name 

#Instance a new database table "once" from python interpreter 
#Type "python" in terminal
#>> from app import db,app
#>> db.init_app(app=app)
#>> with app.app_context():
#....   db.create_all()  
#>> exit()

class Customer(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(255))
    address = db.Column(db.Text)
    notes = db.Column(db.Text)

    def __repr__(self):
        return f'<Customer {self.name}>'

class Interaction(db.Model):
    __tablename__ = 'interactions'
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    interaction_type = db.Column(db.String(255), nullable=False)
    interaction_date = db.Column(db.DateTime, nullable=False)
    notes = db.Column(db.Text)

    customer = db.relationship('Customer', backref=db.backref('interactions', lazy=True))


class Product(db.Model):
  __tablename__ = 'products'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String, nullable=False)
  quantity = db.Column(db.Integer, nullable=False)
  price = db.Column(db.Float, nullable=False)

class Order(db.Model):
  __tablename__ = 'orders'
  id = db.Column(db.Integer, primary_key=True)
  customer_name = db.Column(db.String, nullable=False)
  product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
  product = db.relationship('Product', backref=db.backref('orders', lazy=True))
  quantity = db.Column(db.Integer, nullable=False)
  status = db.Column(db.String, nullable=False)



