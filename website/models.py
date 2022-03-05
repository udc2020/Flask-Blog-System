from sqlalchemy.sql import func
from . import db
from flask_login import UserMixin




# User database 
class User (db.Model,UserMixin):
   """ User Tbable use UserMixin  """
   id = db.Column(db.Integer,primary_key=True)
   email = db.Column(db.String(200),unique=True)
   user_name = db.Column(db.String(100),unique=True)
   password = db.Column(db.String(100))
   # RelationShip Table 
   post = db.relationship('Post')
  


class Post(db.Model, UserMixin):
   id = db.Column(db.Integer,primary_key=True)
   title = db.Column(db.String())
   tag = db.Column(db.String())
   img = db.Column(db.String())
   content = db.Column(db.String())
   date =  db.Column(db.DateTime(timezone=True),default=func.now())
   # RelationShip Tabel
   user_id = db.Column(db.Integer,db.ForeignKey('user.id'))