from flask import Flask, render_template, url_for, make_response
from markupsafe import escape
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return render_template('profile.html', person=username)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

# OR
# @app.get('/login')
# def login_get():
#     return show_the_login_form()

# @app.post('/login')
# def login_post():
#     return do_the_login()

@app.errorhandler(404)
def page_not_found(error):
    resp = make_response(render_template('page_not_found.html', error=error), 404)
    resp.headers['X-ERROR'] = 'ERRO 404' # add aditional information on response headers
    return resp


if __name__ == '__main__':
    app.run(debug=False)