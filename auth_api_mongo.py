'''
url for using the following parameter
login = http://127.0.0.1:5000/login?email=fsali315@gmail.com&password=12345
signup = http://127.0.0.1:5000/signup?fullname=sayyed&20faisal&20ali&email=fsali315@gmail.com&password=12345
'''

from flask import Flask, request
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from os import environ

app = Flask(__name__)
app.config['SECRET_KEY'] = environ.get('SECRET_KEY')

client = MongoClient(environ.get('MONGO_URI'))
db = client.userdata
myCollection = db.user


@app.route('/login')
def login():
    email = request.args.get('email')
    password = request.args.get('password')

    user_data = myCollection.find_one({"email": email})
    if user_data:
        if check_password_hash(user_data["password"], password):
            return 'login sucessfully'
        else:
            return 'User/password does not match'
    else:
        return 'User not found'


@app.route('/signup')
def signup():
    fullname = request.args.get('fullname')
    email = request.args.get('email')
    password = request.args.get('password')

    user = myCollection.find_one({"email": email})
    if user:
        return 'User already exits'
    else:
        myCollection.insert_one({"fullname": fullname, "email": email,
                                "password": generate_password_hash(password, method='sha256')})
        return 'User created successfully'


if __name__ == '__main__':
    app.run(debug=True)
