import os
from flask import Blueprint ,render_template ,request
from flask_login import login_required ,current_user
from website import create_app ,db
from werkzeug.utils import secure_filename
from .models import Post ,User

# Create Vue 
views = Blueprint('views',__name__) 



# Home Page 
@views.route("/")
def home_Page():
   # Get All Data From DB
   all_posts = Post.query.all()
   return render_template("home.html",navbar=True ,user=all_posts) 

# about Page 
@views.route("/about")
def about_Page():
   return render_template("about.html",navbar=True) 

# contact Page
@views.route("/contact")
def contact_Page():
   return render_template("contact.html",navbar=True) 

# Post Blog Page
@views.route("/post", methods=['GET','POST'])
@login_required
def post_Page():
   # we must use App To define Upload Folder
   app = create_app()
   # Chek if we have 
   if request.method == "POST":
      # Get Date from Form
      title = request.form.get("titleBlog")
      tag = request.form.get("tags")
      content = request.form.get('content')
      # get Image 
      img = request.files["thumb"]
      # secure name 
      img_name = secure_filename(img.filename)
      #  chek if we have img
      if img :
         # Save image to static 
         img.save( os.path.join(os.getcwd() + "/website/static/img", img_name))
    

      # Add data to Db 
      post = Post(title=title,tag=tag,img=img_name,content=content,user_id=current_user.id)
      
      db.session.add(post)
      db.session.commit()
   

         
      
   return render_template("post.html",navbar=False,user=current_user,) 



# Craete Post link & Vue
@views.route('blog/<int:id>/<string:title>')
def blogs(id,title):
   # get Post
   post = Post.query.filter_by(user_id=id).first()
   # get Author 
   author = User.query.filter_by(id=id).first()
   return render_template("blogPost.html",navbar=True,user=post,author=author.user_name) 


