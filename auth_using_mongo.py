from os import environ
from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
from flask_login import  login_user, login_required, logout_user, LoginManager, current_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin):
    def __init__(self, user_json):
        self.user_json = user_json

    def get_id(self):
        object_id = self.user_json.get('_id')
        return str(object_id)

app = Flask(__name__)
app.config['SECRET_KEY'] = environ.get('SECRET_KEY')

client = MongoClient(environ.get('MONGO_URI'))
db = client.userdata
myCollection = db.user

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    users = myCollection.find_one({"_id":id}) 
    return User(user_json=users)

@app.route('/')
@login_required
def home():
    return render_template('home.html',user=current_user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user_data = myCollection.find_one({"email":email})
        if user_data:
            if check_password_hash(user_data["password"],password):
                flash('Logged in successfully!', category='success')
                loginuser = User(user_data)
                login_user(loginuser,remember=True)
                return redirect(url_for('home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template('login.html',user=current_user)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        fullname = request.form.get('fullname')
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = myCollection.find_one({"email":email})
        if user:
            flash('Email already exists.', category='error')
        else:
            myCollection.insert_one({"fullname":fullname,"email":email,"password":generate_password_hash(password,method='sha256')})
            return redirect(url_for('login'))

    return render_template('signup.html',user=current_user)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
