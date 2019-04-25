from flask import Flask, render_template, url_for
import json

app = Flask(__name__)


def readJsonFile(filename):
    with open(filename) as json_file:
        return json.load(json_file)


filename = readJsonFile('Country_LGA_Suburb Ranked.txt')


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


@app.route('/suburbs')
def suburb():
    return render_template('Suburb.html')


@app.route('/lga/<name>')
def lga(name):
    output = lga_extractor(suburbs_info, name)
    return render_template('Suburb.html', lga=output)


if __name__ == '__main__':
    app.run(debug=True)
