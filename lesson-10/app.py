# import all of the classes and modules we use in this file from the flask package
from flask import Flask, render_template, request
# create an instance of the Flask class with name = __name__ or the name of this file
app = Flask(__name__)

# set debug to true so we see error dumps in the browser
app.debug = True

# decorators to establish the URL route to reach the method below
@app.route('/', methods=['GET'])
@app.route('/<string:name>/<string:color>/<int:age>', methods=['GET'])
def index(name=None, color='blue', age=25):
    # create a list of dictionaries
    data = [{'name':'olivia','color':'red', 'age':26},
             {'name':'tom','color':'green', 'age':34}]
    # add values from URL if present
    if name is not None:
        data.append({'name':name,'color': color, 'age':age})
    # renders index.html from templates directory, passing in the names variable
    return render_template('index.html', data=data)

# decorators to establish the URL route to reach the method below, accepts GET and POST
@app.route('/post', methods=['GET','POST'])
def post():
    # checks if request method is POST
    if request.method == 'POST':
        # POST data is contained in request.form['variable_name']
        full_name = request.form['firstname'] + " " + request.form['lastname']
        return render_template("post.html", name=full_name)
    else:
        # otherwise another request method, probably a GET
        return render_template("post.html")

# launch the app
app.run()