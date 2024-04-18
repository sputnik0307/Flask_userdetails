# from flask import Flask,request, render_template

# app = Flask(__name__)

# @app.route("/")
# def homePage():
#     return "This is the home page of our website."

# users = []

# @app.route("/add_user", methods=['GET', 'POST'])
# def add_user():
#     if request.method == 'POST':
#         full_name = request.form['full_name']
#         email = request.form['email']
#         user_data = {'full_name': full_name, 'email': email}
#         users.append(user_data)
#         return f"User added successfully: {full_name}, {email}"
#     else:
#         return render_template('index.html')

# @app.route("/display_user", methods=['GET'])
# def display_user():
#      return render_template('displayUser.html', users=users)


# if __name__ == "__main__":
#     app.run(debug=True)



from flask import Flask, request, render_template

app=Flask(__name__)

@app.route("/")
def homepage():
    return (render_template('index.html'))

users =[]
@app.route('/add_user', methods=['GET','POST'])
def add_user():
    if request.method=='POST':
        fullname=request.form['full_name']
        email=request.form['email']
        #converting into dicitonary
        user_list={'full_name':fullname,'email':email}
        users.append(user_list)
        return f"User added successfully : \nFull Name: {fullname},\nEmail    : {email}"
    else:
        return render_template("index.html",users=users)
    
@app.route('/display_user',methods=['GET'])
def display_user():
    return render_template("displayUser.html",users=users)

if __name__ == "__main__":
    app.run(debug=True)

