# Web Development
Popular web frameworks for python are Flask & Djanko.  
## Flask
Light weight web frame work for python. [Ref](https://flask.palletsprojects.com/en/2.0.x/quickstart/)
### Sample
```
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"
```
save file as server.py  

### Run server
`export FLASK_APP=server`  
for debug mode(optional): `export FLASK_ENV=development`  
`flask run`  
OR    
`python3 -m flask run`

### Usage
1. Html files should be placed inside `templates` folder.
2. JS & CSS files should be placed inside `static` folder.

Resources
---------
* [Free HTML templates](http://www.mashup-template.com/templates.html)
