from website import create_app

# Mian App 
app = create_app()



if __name__ == "__main__":
   app.run(debug=True)