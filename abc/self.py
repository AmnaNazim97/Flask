from flask import Flask
self = Flask(__name__)


username=[
    {
        "name":"Amna",
        "password" : "abc"
    },
    {
        "name":"Zoya",
        "password":"abcsd"
    },
    {
        "name":"John",
        "password":"pole"
    },
    {
        "name":"alex",
        "password":"aqsad"
    }
]

from flask_pymongo import PyMongo
self.config['MONGO_URI'] = 'mongodb+srv://amna_nazim:amna123@cluster1-aipmq.mongodb.net/test?retryWrites=true&w=majority'
#@app.route("/test", methods=['POST'])'

mongo = PyMongo(self)

@self.route('/ok')
def inndex():
    usersdata = mongo.db.usersdata
    result = usersdata.find_one({"username":"ali"}, {'id': 0})
    print(mongo.db.usersdata)
    return 'Hello !'

@self.route("/find")
def finddata():
    usersdata = mongo.db.usersdata
    result = usersdata.find({})
    for i in result:
        data.append(i)
    return ()

@self.before_request()
def bef():
    print('Hello zoya :)')

@self.route('/')
def hello_world():
    return 'We did it :)'

@self.route('/okay')
def index():
    username= request.cookies.get('username')

from flask import make_response

@self.route('/')
def indexx():
    resp = make_response(render_template(...))
    resp.set_cookie('username', 'the username')
    return resp

@self.route('/hello')
def hello():
    return 'Heya! '

@self.route('/project/')
def project():
    return 'This is project page'

@self.route('/about')
def about():
    return 'About Us'

from flask import request 
@self.route('/login', methods=['POST', 'GET'])
def login():
    if request.method =='POST':
        return do_the_login()
    else:
        return 'show_the_login_form'

from flask import abort , redirect , url_for , jsonify

@self.route('/this')
def this():
    return redirect(url_for('login'))

from flask import request

@self.route('/loginn')
def loginnn():
    abort(401)
    this_is_never_executed()

@self.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

@self.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp

@self.route('/me')
def my_api():
    user= get_current_user()
    return{
        "ayesha":user.ayesha,
        "theme":user.theme
    }

@self.route('/users')
def users_api():
    users = get_all_users()
    return jsonify([user.to_json() for user in users])
from flask import session


#@self.route('/upload', methods=['GET', 'POST'])
#def upload_file():
    #if request.method == 'POST':
        #f = request.files['uploadfile']
        #f.save('/var/www/uploads/uploadfile.txt')

with self.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'

#with self.request_context(environ):
 #   assert request.method == 'POST'


from flask import render_template , escape , url_for

@self.route('/hello/')
@self.route('/hello/name')
def hey(name=None):
    return render_template('username.html', name=name)

from flask import Markup
Markup('<strong>Hello %s!</strong>')% '<blink>hacker</blink>'
Markup.escape('<blink>hacker</blink>')
Markup('<em>Marked up</em> &raquo; HTML').striptags()

@self.route('/user/<username>')
def show_user_profile(username):
    return 'User%s' %escape(username)
@self.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

#with self.test_request_context():
 #   print(url_for('index'))
  #  print(url_for('login'))
   # print(url_for('login', next='/'))
    #print(url_for('/profile', username='John'))


@self.route('/post/<int:post_id>')
def show_post(post_id):
    return 'post%d' % post_id

@self.route('/path/<path:subpath>')
def show_subpath(subpath):
    return 'Subpath%s' %escape(subpath)

@self.route('/login', methods=['POST', 'GET'])
def loginn():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('loginn.html', error=error)




if __name__ == "__main__":
    self.run(debug=True , port=1088)