from importlib.resources import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


# Create Database 
db = SQLAlchemy()


def create_app():
   
   app = Flask(__name__)
   
   # configs
   app.config['SECRET_KEY'] = 'ultrasdzcoder'
   app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
   app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
   
   # Uplaod to img Folder
   app.config["UPLOAD_FOLDER"] = "website/static/img"

   
   # config DATABASE
   db.init_app(app)
   
   # MVT
   from .views import views   
   from .auth import auth   
   
   # Create Initial Routers
   app.register_blueprint(views,url_prefix="/")
   app.register_blueprint(auth,url_prefix="/")
   
   # import Tables From Database
   from .models import User ,Post
   
   create_db(app)
   
   # For Login System Use login Manager
   login_manager = LoginManager()
   login_manager.login_view = 'auth.login_Page'
   login_manager.init_app(app)
   
   @login_manager.user_loader
   def load_user(id):
      return User.query.get(int(id))
   
  
   
   return app 




def create_db(APP):
   # Check if database in directoury
   if not path.exists('website/database.db'):
      db.create_all(app=APP)
      print("Create DB!")