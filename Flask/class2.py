from flask import Flask , render_template , redirect , request , jsonify
from flask_pymongo import PyMongo
import bcrypt

app = Flask(__name__)
app.config["MONGO_URI"]= 'mongodb+srv://amna_nazim:amna123@cluster1-aipmq.mongodb.net/test?retryWrites=true&w=majority'
#@app.route("/test", methods=['POST'])

mongo = PyMongo(app)
print(mongo)


@app.route('/signupauth', methods=['POST'])
def signupauth():
    data= dict(request.form)
    print(data)
    usersdata = mongo.db.usersdata
    result = usersdata.find_one({"email": data['email']})
    print(result)
    if(result):
        return redirect('/login')

