from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:ChristmasTime@localhost/History_Schema'
db = SQLAlchemy(app)

class Table(db.Model):
    __tablename__ = 'Ingredients'
    name = db.Column('Name', db.String, primary_key =True)
    itype = db.Column('Type', db.String)

@app.route('/')
@app.route('/home')
def home():
    #return '<h1>Home Page</h1>'
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)