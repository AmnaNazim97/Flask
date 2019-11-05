from flask import Flask,render_template

app = Flask(__name__)

@app.route('/showhtml')
def showhtml():
    return render_template("index.html")
if __name__ == "main":
    app.run(debug=True,port=8081)
    