from distutils.log import error
from flask import Blueprint , render_template , request ,redirect, url_for
from .models import User 
from werkzeug.security import generate_password_hash ,check_password_hash
from website import db
from flask_login import login_user,logout_user , login_required ,current_user

# Create Authuntication 
auth = Blueprint('auth',__name__) 


# Sign Up Page 
@auth.route("/signin" , methods=['GET','POST'])
def signin_Page():
   # chek if have Problems 
   error = False
   # Check th request 
   if request.method == "POST":
      # Get Data from Form 
      user_name = request.form.get('user')
      email = request.form.get('email')
      password = request.form.get('password')
      
      # is User name unique ?
      isEmailUniq = User.query.filter_by(user_name=user_name).first()

      if isEmailUniq :
         error = True
      else:
         # Add Data To User Table (DB)
         # use hash protected password
         user = User(user_name=user_name,email=email,password=generate_password_hash(password,method="sha256"))

         # Save Data
         db.session.add(user)
         db.session.commit()

         # Make user logged 
         login_user(user,remember=True)
         
         return redirect(url_for("views.home_Page"))
      
      
   return render_template("signin.html" ,navbar=True,error=error,user=current_user) 


# Login Page 
@auth.route("/login" , methods=['GET','POST'])
def login_Page():
   # check errors
   error = False
   # chek Request
   if request.method == "POST":
      # get data from FORM
      user_name = request.form.get('user')
      password = request.form.get('password')
      # selct one result
      user = User.query.filter_by(user_name=user_name).first()
      #chek if we have user
      if user :
         # DeCrypt password & chek irt 
         if check_password_hash(user.password,password):
            login_user(user,remember=True)
            return redirect(url_for('views.post_Page'))
         else:
            error = True
      else:error = True

   return render_template("login.html" ,navbar=True,error=error,user=current_user) 

# Log Out Page
@auth.route("/logout")
@login_required #to make this route private
def logout_Page():
   logout_user()
   return redirect(url_for('auth.login_Page'))  

