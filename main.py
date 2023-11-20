from flask import Flask,render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def main():
    year = datetime.now().year
    name = "viacheslav"
    random_number = random.randint(1,10)
    return render_template('index.html', number=random_number, time=year, name=name)

@app.route('/guess/<guess>')
def guess_name(guess):
    # gender
    response_gender = requests.get(f'https://api.genderize.io?name={guess}')
    response_age = requests.get(f'https://api.agify.io?name={guess}')
    print(response_age.json())
    print(response_gender.json())
    sex = response_gender.json()['gender']
    age = response_age.json()['age']
    name = guess
    return render_template("write.html",age=age ,sex=sex ,name=name)
    return "<h1>guess</h1>"

app.run()

