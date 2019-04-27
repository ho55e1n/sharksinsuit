from flask import Flask, render_template, url_for
import json
import os


script_dir = os.path.dirname(__file__)
rel_path = "Country_LGA_Suburb Ranked.txt"
abs_file_path = os.path.join(script_dir, rel_path)

app = Flask(__name__)


def readJsonFile(filename):
    with open(filename) as json_file:
        return json.load(json_file)


filename = readJsonFile(abs_file_path)


def getByNationality(filename, countryname):
    output = []

    for item in filename:
        if item["Country"] == countryname:
            # item.pop("Country")
            # item.pop("Info")
            output.append(item)

    return output


china = getByNationality(filename, "China")
india = getByNationality(filename, "India")
iran = getByNationality(filename, "Iran")
suburbs_info = readJsonFile('data.txt')['all_suburbs']
events_info = readJsonFile('events.txt')['events']


def lga_extractor(filename, param):
    for entry in filename:
        if entry['name'] == param:
            return entry
    return {}


@app.route('/')
def index2():
    return render_template('index.html')


@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/profile-China')
def profile_china():
    return render_template('profile-China.html', nationality=china)


@app.route('/profile-India')
def profile_india():
    return render_template('profile-India.html', nationality=india)


@app.route('/profile-Iran')
def profile_iran():
    return render_template('profile-Iran.html', nationality=iran)


@app.route('/profile')
def suburb():
    return render_template('profile-noNationality-1.html')


@app.route('/lga/<name>')
def lga(name):
    output = lga_extractor(suburbs_info, name)
    return render_template('Suburb.html', lga=output)


@app.route('/test')
def testing_page():
    return render_template('untitled.html', events=events_info)


if __name__ == '__main__':
    app.run(debug=True)
