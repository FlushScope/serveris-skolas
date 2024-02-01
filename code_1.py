from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    class_name = db.Column(db.String(10), nullable=False)
    pk = db.Column(db.String(10), nullable=False)

class Computer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    electronic_number = db.Column(db.String(100), nullable=False)
    model_name = db.Column(db.String(100), nullable=False)
    box_number = db.Column(db.String(100), nullable=False)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    computer_id = db.Column(db.Integer, db.ForeignKey('computer.id'), nullable=False)
    hand_out_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    hand_in_time = db.Column(db.DateTime)

@app.route('/')
def home():
    students = Student.query.all()
    computers = Computer.query.all()
    return render_template('index.html', students=students, computers=computers)

# Add routes for other functionalities here

if __name__ == '__main__':
    app.run(debug=True)