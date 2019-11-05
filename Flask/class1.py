from flask import Flask , render_template , redirect , request , jsonify
from flask_pymongo import PyMongo
app = Flask(__name__)
app.config["MONGO_URI"]= 'mongodb+srv://amna_nazim:amna123@cluster1-aipmq.mongodb.net/test?retryWrites=true&w=majority'
#@app.route("/test", methods=['POST'])

mongo = PyMongo(app)
print(mongo)


@app.route('/')
def index():
    return jsonify({"msg": 'Hello from my side'})

@app.route('/login')
def login():
    return render_template('login.html')

users = [
    {
        "name": "amna",
        "password " : "abc"

    },
    {
        "name": "zoya",
        "password" : " abcd"
    },
    {
        "name" : "khansa",
        "password" : "abc1"
    },
    {
        "name":"hufsa",
        "password" : "abcd1"
    }
    ]



@app.route('/')
#def index():
 #   return jsonify({"message: hello friends" , "users" : users})

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/home')
def home():
    return "Hello from Home Page"

@app.route('/signupAuth', methods=["POST"])
def signup_auth():
    data=  dict(request.form)
    print(data)
    usersData=mongo.db.usersData
    result = usersData.find({})
    for i in result:
        print(i)
    #usersData.insert_one(data)
    return redirect('/login')

def test(): 
    data = request.form
    data = dict(data)
    # for i , v in enumerate(users):
    #     if (data["username"]==v["name"] and data["password"] == v["password"]):
    #         login = mongo.db.login
    #         login.insert_one(data)

            
    #         return redirect("http://127.0.0.1:1006/home")
    return redirect("http://127.0.0.1:1006/login")

@self.route('/post' )
    

if __name__ == "__main__":
    app.run(debug=True , port=1006)
    