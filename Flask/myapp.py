from flask import Flask,render_template, request , redirect

app=Flask(__name__)

@app.route("/")
def home():
    return "Hello"

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/home')
def home1():
    return " this is home page"

@app.route("/auth", methods=["Post"])
def auth():
    data = request.form
    if(data['username'] =='Amna' and data['password']=="Pakistan"):
        return redirect('/home')
    else:
        return redirect('/login')

if __name__=="__main__":
    app.run(debug= True , port=8088)
