from flask import Flask, render_template, url_for, send_from_directory
import os

app = Flask(__name__)


@app.route("/")
def home_page():
    """Home page."""
    return render_template('index.html')


@app.route("/<username>")
def about_page(username=None, id=0):
    """About page."""
    return render_template('about.html', name=username, identity_num=id)


@app.route("/<username>/<int:id>")
def id_page(username=None, id=None):
    """About page."""
    return render_template('about.html', name=username, identity=id)
