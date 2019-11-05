from flask import Flask , render_template , redirect , request
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome home"

@app.roue('/loginn')
def login():
    return render_template('abcd.html')

users=[
    {
        "name:ali"
        "password:abcd"},
    {
        'name=osama'
        'password:abc'},
    {
        'name=arish'
        'password:abc1'
        },

    }
    }

}]

def authr():
    data = request.form
    for i, v in enumerate(users):
        if (data['username']==v['name'] and data['password']
        ==v['password']):
        print(i)
        return redirect('/home')
return redirect('/login')
