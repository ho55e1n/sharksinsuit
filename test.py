from flask import Flask, render_template, url_for, redirect, request
import json
import os


script_dir = os.path.dirname(__file__)
rel_path = "Country_LGA_Suburb Ranked.txt"
abs_file_path = os.path.join(script_dir, rel_path)

app = Flask(__name__)


def readJsonFile(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    final_filename = os.path.join(script_dir, filename)
    with open(final_filename, encoding="utf-8-sig") as json_file:
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


def get_header(item):
    out = item['LGA Name']
    return out


china = getByNationality(filename, "China")
india = getByNationality(filename, "India")
iran = getByNationality(filename, "Iran")
suburbs_info = readJsonFile('data.txt')['all_suburbs']
chinese_events_info = readJsonFile('chinese_events.txt')['events']
indian_events_info = readJsonFile('indian_events.txt')['events']
iranian_events_info = readJsonFile('iranian_events.txt')['events']
rent_lga = readJsonFile("LGA rent.txt")['lga']
lga_final = readJsonFile("LGA_COMPARE_FINAL.json.txt")['lga']
lga_name_list = list(map(get_header, lga_final))
lga_info = readJsonFile("LGA_FINAL_3.json.txt")['lga']


def lga_extractor(filename, key, param):
    for entry in filename:
        if entry[key] == param:
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


@app.route('/events-default')
def suburb():
    return render_template('profile-noNationality-1.html')


@app.route('/lga/<name>', methods=['GET', 'POST'])
def lga(name):
    output = lga_extractor(lga_info, 'LGA Name', name)
    return render_template('Suburb.html', lga=output)


@app.route('/council')
def council():
    return render_template('Suburb.html')


@app.route('/events/<name>')
def events(name):
    if name == "china":
        return redirect(url_for('events_chinese'))
    if name == "iran":
        return redirect(url_for('events_iranian'))
    if name == "india":
        return redirect(url_for('events_indian'))


@app.route('/events_chinese')
def events_chinese():
    return render_template('events_chinese.html', events=chinese_events_info)


@app.route('/events_iranian')
def events_iranian():
    return render_template('events_iranian.html', events=iranian_events_info)


@app.route('/events_indian')
def events_indian():
    return render_template('events_indian.html', events=indian_events_info)


@app.route('/events-new')
def events_new():
    return render_template('events-new.html', events=chinese_events_info)


@app.route('/test')
def testing_page():
    return render_template('untitled.html', events=chinese_events_info)


@app.route('/compare')
def compare():
    return render_template('compare.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        lga_brand = request.form.get("cars", None)
        lga_brand2 = request.form.get("motors", None)
        if (lga_brand and lga_brand2) != None:
            rent = lga_extractor(rent_lga, 'LGA', lga_brand)
            rent2 = lga_extractor(rent_lga, 'LGA', lga_brand2)
            return render_template("compare.html", car_brand=rent, motor_brand=rent2)
    return render_template("compare.html")


@app.route('/comparetwo')
def comparetwo():
    return render_template('comparetwo.html', lga_name=lga_name_list)


@app.route('/success', methods=['GET', 'POST'])
def success():
    if request.method == "POST":
        lga_brand = request.form.get("cars", None)
        lga_brand2 = request.form.get("motors", None)
        if (lga_brand and lga_brand2) != None:
            rent = lga_extractor(lga_final, 'LGA Name', lga_brand)
            rent2 = lga_extractor(lga_final, 'LGA Name', lga_brand2)
            return render_template("comparetwo.html", c1=rent, c2=rent2, lga_name=lga_name_list)
    return render_template("comparetwo.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
