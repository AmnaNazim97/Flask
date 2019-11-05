from flask import Flask , render_template
app = Flask(__name__)
print(__name__)

@app.route('/')
def index():
    return """
    <h1>okay !</h2>
    <h1>next time!</h2>
    <h1>hungry !</h2>
    <h1>patience :) </h2>
    <h1>Why this ?!</h2>
    <h1>bye!</h2>
    """

@app.route("/showhtml")
def showhtml():
    return render_template('index.html')   

@app.route('/login')
def login():
    return """    <h1>Welcome </h1>
    <h1>Think Less </h1>
    <h1>Work more</h1>
    <h1>Stay calm </h1>
    <h1>Goodbye</h1>
    """

@app.route('/login/<name>')
def login2(name):
    return "Hello from login user" + name

if __name__ == "__main__":
    app.run(debug = True , port = 8080)
