import os

from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template("index.html")

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/#success')
        except:
            return 'Did not save to database'
    else:
        return 'Something went wrong. Try again!'

def write_to_csv(data):
    file_exist = os.path.isfile('database.csv')
    with open('database.csv', mode='a', newline='') as database:
        fieldnames = ['name', 'email', 'message']
        csv_writer = csv.DictWriter(database, fieldnames=fieldnames)
        if not file_exist:
            csv_writer.writeheader()
        csv_writer.writerow(data)
