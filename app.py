# imports app object from ./application/__init__.py
from application import app
# if the file is being run directly, and not imported, then start the application. 
if __name__ == '__main__':
 app.run(debug=True, host='0.0.0.0')

from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title ="Home Page")
@app.route('/about')
def about():
    return render_template('about.html', title = "About Page")

