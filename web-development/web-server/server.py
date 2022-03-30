"""Flask server code sample."""
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home_page():
    """Home page."""
    return render_template('index.html')


@app.route("/about.html")
def about_page(username="Jerin", idx=101):
    """About page."""
    return render_template('about.html', name=username, identity=idx)


@app.route("/<username>/<int:id>")
def id_page(username=None, idx=None):
    """About page with dynamic data from url."""
    return render_template('about.html', name=username, identity=idx)


@app.route("/registration.html")
def reg_page():
    """Registration Page."""
    return render_template('registration.html')


@app.route("/register", methods=['POST', 'GET'])
def registration(username=None, idx=None):
    """Get form data."""
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        username = data['name']
        idx = data['id']
        response = "Registration Sucess"
        return render_template(
            'about.html', name=username, identity=idx, response=response)
    else:
        response = "Registration Failed"
    return response
