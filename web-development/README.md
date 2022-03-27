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
3. [Request Handling](https://flask.palletsprojects.com/en/2.0.x/quickstart/#the-request-object)

### Tip:
1. Setting up Virtual Environment  
`python3 -m venv /path/to/venv`  
* https://docs.python.org/3/library/venv.html  
2. Generating Requirements file using pip3  
`pip3 freeze > requirements.txt`  

Resources
---------
1. Free HTML templates:
* http://www.mashup-template.com/templates.html
* https://html5up.net/ 
* https://www.creative-tim.com/bootstrap-themes/ui-kit?direction=asc&sort=price
2. Free Website hosting:
* [Python anywhere](https://help.pythonanywhere.com/pages/Flask/)
3. Sample:
* https://github.com/aneagoie/portfo
4. Web development tutorial
* https://www.w3schools.com/html/default.asp 
5. Selenium: Browser Automation
* https://selenium-python.readthedocs.io/
* [selenium python cheat sheet](http://allselenium.info/python-selenium-commands-cheat-sheet-frequently-used/)
* [practice browser testing here](https://demo.seleniumeasy.com/)