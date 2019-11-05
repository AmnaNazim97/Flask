from flask import Flask , render_template , redirect , request

app = Flask(__name__)

@app.route("/test", methods=['POST'])

def test():
    return "Hello world!"

if __name__ == "__main__":
    app.run(debug=True , port=1006)
