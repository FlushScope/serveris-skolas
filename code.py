# app.py
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    classes = ['10.CV', '10.ES', '10.EU', '10.IT', '11.CV', '11.EI', '11.EU', '11.SA', '12.CV', '12.EU', '12.SA', '12.VI']
    students = {'10.CV': ['Student1', 'Student2', 'Student3']}
    computers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    return render_template('index.html', classes=classes, students=students, computers=computers)

if __name__ == '__main__':
    app.run(debug=True)