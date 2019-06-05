from flask import Flask, render_template, url_for, redirect, request, jsonify
import requests
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import json
import os

script_dir = os.path.dirname(__file__)
app = Flask(__name__)


# relative project directory
basedir = os.path.abspath(os.path.dirname(__file__))
# Database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)


# Suburb Class/Model
class Suburb(db.Model):
    __tablename__ = "suburbs"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    lga = db.Column(db.String(100))
    postcode = db.Column(db.Integer)

    def __init__(self, postcode, name, lga):
        self.postcode = postcode
        self.name = name
        self.lga = lga


# Event Class/Model
class Event(db.Model):
    __tablename__ = "events"
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer)
    name_text = db.Column(db.String(100))
    description_text = db.Column(db.String(2000))
    summary = db.Column(db.String(1000))
    url = db.Column(db.String(1000))
    start_date = db.Column(db.String(100))
    start_time = db.Column(db.String(100))
    end_date = db.Column(db.String(100))
    end_time = db.Column(db.String(100))
    venue_id = db.Column(db.Integer)
    logo_original = db.Column(db.String(1000))
    community = db.Column(db.String(100))
    location = db.Column(db.String(100))

    def __init__(self, event_id, name_text, description_text, summary, url, start_date, start_time, end_date, end_time, venue_id, logo_original, community, location):
        self.event_id = event_id
        self.name_text = name_text
        self.description_text = description_text
        self.summary = summary
        self.url = url
        self.start_date = start_date
        self.start_time = start_time
        self.end_date = end_date
        self.end_time = end_time
        self.venue_id = venue_id
        self.logo_original = logo_original
        self.community = community
        self.location = location


# LGA Class/Model
class Lga(db.Model):
    __tablename__ = "lga"
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(100))
    info = db.Column(db.String(100))
    suburb = db.Column(db.String(100))

    def __init__(self, country, info, suburb):
        self.country = country
        self.info = info
        self.suburb = suburb


# # Info lga Class/Model
class Info(db.Model):
    __tablename__ = "lga_info"
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(40))
    Distance = db.Column(db.String(10))
    Time = db.Column(db.String(30))
    Birth_country_1 = db.Column(db.String(10))
    percent_country_1 = db.Column(db.String(10))
    Birth_country_2 = db.Column(db.String(10))
    percent_country_2 = db.Column(db.String(10))
    Birth_country_3 = db.Column(db.String(10))
    percent_country_3 = db.Column(db.String(10))
    Birth_country_4 = db.Column(db.String(10))
    percent_country_4 = db.Column(db.String(10))
    Birth_country_5 = db.Column(db.String(10))
    percent_country_5 = db.Column(db.String(10))
    language_1 = db.Column(db.String(10))
    language_2 = db.Column(db.String(10))
    language_3 = db.Column(db.String(10))
    language_4 = db.Column(db.String(10))
    language_5 = db.Column(db.String(10))
    Unemployment_rate = db.Column(db.String(30))
    Unemployment_rank = db.Column(db.Integer)
    RentID = db.Column(db.String(30))
    RentName = db.Column(db.String(50))
    CrimeID = db.Column(db.String(30))
    CrimeName = db.Column(db.String(50))
    AmulanceID = db.Column(db.String(30))
    AmbulanceName = db.Column(db.String(50))

    def __init__(self, Name, Distance, Time, Birth_country_1, percent_country_1, Birth_country_2, percent_country_2, Birth_country_3, percent_country_3, Birth_country_4, percent_country_4, Birth_country_5, percent_country_5, language_1, language_2, language_3, language_4, language_5, Unemployment_rate, Unemployment_rank, RentID, RentName, CrimeID, CrimeName, AmulanceID, AmbulanceName):
        self.Name = Name
        self.Distance = Distance
        self.Time = Time
        self.Birth_country_1 = Birth_country_1
        self.percent_country_1 = percent_country_1
        self.Birth_country_2 = Birth_country_2
        self.percent_country_2 = percent_country_2
        self.Birth_country_3 = Birth_country_3
        self.percent_country_3 = percent_country_3
        self.Birth_country_4 = Birth_country_4
        self.percent_country_4 = percent_country_4
        self.Birth_country_5 = Birth_country_5
        self.percent_country_5 = percent_country_5
        self.language_1 = language_1
        self.language_2 = language_2
        self.language_3 = language_3
        self.language_4 = language_4
        self.language_5 = language_5
        self.Unemployment_rate = Unemployment_rate
        self.Unemployment_rank = Unemployment_rank
        self.RentID = RentID
        self.RentName = RentName
        self.CrimeID = CrimeID
        self.CrimeName = CrimeName
        self.AmulanceID = AmulanceID
        self.AmbulanceName = AmbulanceName


# Compare Councils Class/Model
class Compare(db.Model):
    __tablename__ = "lga_compare"
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(40))
    Distance = db.Column(db.String(10))
    Time = db.Column(db.String(30))
    Suburb_1 = db.Column(db.String(25))
    Suburb_2 = db.Column(db.String(25))
    Suburb_3 = db.Column(db.String(25))
    Suburb_4 = db.Column(db.String(25))
    Suburb_5 = db.Column(db.String(25))
    Population = db.Column(db.String(10))
    Population_density = db.Column(db.String(10))
    Overseas_rank = db.Column(db.String(10))
    Unemployment_rate = db.Column(db.String(30))
    One_br_flat = db.Column(db.Integer)
    Two_br_flat = db.Column(db.Integer)
    Three_br_flat = db.Column(db.Integer)
    Two_br_house = db.Column(db.Integer)
    Three_br_house = db.Column(db.Integer)
    Four_br_house = db.Column(db.Integer)
    Tram = db.Column(db.String(3))
    Bus = db.Column(db.String(3))
    Train = db.Column(db.String(3))
    Crime_against_person = db.Column(db.Integer)
    Property_offences = db.Column(db.Integer)
    Drug_offences = db.Column(db.Integer)
    Public_order_offences = db.Column(db.Integer)
    Justice_procedures_offences = db.Column(db.Integer)
    Other_offences = db.Column(db.Integer)
    Ambulance_response = db.Column(db.String(10))

    def __init__(self, Name, Distance, Time, Suburb_1, Suburb_2, Suburb_3, Suburb_4, Suburb_5, Population, Population_density, Overseas_rank, Unemployment_rate, One_br_flat, Two_br_flat, Three_br_flat, Two_br_house, Three_br_house, Four_br_house, Tram, Bus, Train, Crime_against_person, Property_offences, Drug_offences, Public_order_offences, Justice_procedures_offences, Other_offences, Ambulance_response):
        self.Name = Name
        self.Distance = Distance
        self.Time = Time
        self.Suburb_1 = Suburb_1
        self.Suburb_2 = Suburb_2
        self.Suburb_3 = Suburb_3
        self.Suburb_4 = Suburb_4
        self.Suburb_5 = Suburb_5
        self.Population = Population
        self.Population_density = Population_density
        self.Overseas_rank = Overseas_rank
        self.Unemployment_rate = Unemployment_rate
        self.One_br_flat = One_br_flat
        self.Two_br_flat = Two_br_flat
        self.Three_br_flat = Three_br_flat
        self.Two_br_house = Two_br_house
        self.Three_br_house = Three_br_house
        self.Four_br_house = Four_br_house
        self.Tram = Tram
        self.Bus = Bus
        self.Train = Train
        self.Crime_against_person = Crime_against_person
        self.Property_offences = Property_offences
        self.Drug_offences = Drug_offences
        self.Public_order_offences = Public_order_offences
        self.Justice_procedures_offences = Justice_procedures_offences
        self.Other_offences = Other_offences
        self.Ambulance_response = Ambulance_response


# Suburb Schema


class SuburbSchema(ma.Schema):
    class Meta:
        fields = ('id', 'postcode', 'name', 'lga')

# lga Schema


class LgaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'country', 'info', 'suburb')

# event Schema


class EventSchema(ma.Schema):
    class Meta:
        fields = ('id', 'event_id', 'name_text', 'description_text', 'summary', 'url', 'start_date',
                  'start_time', 'end_date', 'end_time', 'venue_id', 'logo_original', 'community', 'location')

# Info lga schema


class InfoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'Name', 'Distance', 'Time', 'Birth_country_1', 'percent_country_1', 'Birth_country_2', 'percent_country_2', 'Birth_country_3', 'percent_country_3', 'Birth_country_4',
                  'percent_country_4', 'Birth_country_5', 'percent_country_5', 'language_1', 'language_2', 'language_3', 'language_4', 'language_5', 'Unemployment_rate', 'Unemployment_rank', 'RentID', 'RentName', 'CrimeID', 'CrimeName', 'AmulanceID', 'AmbulanceName')


class CompareSchema(ma.Schema):
    class Meta:
        fields = ('id', 'Name', 'Distance', 'Time', 'Suburb_1', 'Suburb_2', 'Suburb_3', 'Suburb_4', 'Suburb_5', 'Population', 'Population_density',
                  'Overseas_rank', 'Unemployment_rate', 'One_br_flat', 'Two_br_flat', 'Three_br_flat', 'Two_br_house', 'Three_br_house', 'Four_br_house', 'Tram', 'Bus', 'Train', 'Crime_against_person', 'Property_offences', 'Drug_offences', 'Public_order_offences', 'Justice_procedures_offences', 'Other_offences', 'Ambulance_response')

# Create a Suburb via POST request using postman


@app.route('/suburb',  methods=['POST'])
def add_suburb():
    req = request.get_json()["all_suburbs"]
    # print(req[0]['name'])
    for r in req:
        postcode = r['postcode']
        name = r['name']
        lga = r['lga']

        new_suburb = Suburb(postcode, name, lga)

        db.session.add(new_suburb)
        db.session.commit()

    return suburbs_schema.jsonify(new_suburb)

# Create Info LGA
@app.route('/info_lga',  methods=['POST'])
def add_info_lga():
    req = request.get_json()["lga"]
    for r in req:
        name = r['Name']
        distance = r['Distance']
        time = r['Time']
        birth_country_1 = r['Birth_country_1']
        percent_country_1 = r['percent_country_1']
        birth_country_2 = r['Birth_country_2']
        percent_country_2 = r['percent_country_2']
        birth_country_3 = r['Birth_country_3']
        percent_country_3 = r['percent_country_3']
        birth_country_4 = r['Birth_country_4']
        percent_country_4 = r['percent_country_4']
        birth_country_5 = r['Birth_country_5']
        percent_country_5 = r['percent_country_5']
        language_1 = r['language_1']
        language_2 = r['language_2']
        language_3 = r['language_3']
        language_4 = r['language_4']
        language_5 = r['language_5']
        unemployment_rate = r['Unemployment_rate']
        unemployment_rank = r['Unemployment_rank']
        crimeID = r['CrimeID']
        crimeName = r['CrimeName']
        rentID = r['RentID']
        rentName = r['RentName']
        amulanceID = r['AmulanceID']
        ambulanceName = r['AmbulanceName']

        new_info = Info(name, distance, time, birth_country_1, percent_country_1, birth_country_2, percent_country_2, birth_country_3, percent_country_3, birth_country_4, percent_country_4, birth_country_5,
                        percent_country_5, language_1, language_2, language_3, language_4, language_5, unemployment_rate, unemployment_rank, crimeID, crimeName, rentID, rentName, amulanceID, ambulanceName)

        db.session.add(new_info)
        db.session.commit()

    return infos_schema.jsonify(new_info)


# Create compare lga
@app.route('/addcompare',  methods=['POST'])
def add_compare_lga():
    req = request.get_json()["lga"]
    for r in req:
        name = r['Name']
        distance = r['Distance']
        time = r['Time']
        suburb_1 = r['Suburb_1']
        suburb_2 = r['Suburb_2']
        suburb_3 = r['Suburb_3']
        suburb_4 = r['Suburb_4']
        suburb_5 = r['Suburb_5']
        population = r['Population']
        population_density = r['Population_density']
        overseas_rank = r['Overseas_rank']
        unemployment_rate = r['Unemployment_rate']
        one_br_flat = r['One_br_flat']
        two_br_flat = r['Two_br_flat']
        three_br_flat = r['Three_br_flat']
        two_br_house = r['Two_br_house']
        three_br_house = r['Three_br_house']
        four_br_house = r['Four_br_house']
        tram = r['Tram']
        bus = r['Bus']
        train = r['Train']
        crime_against_person = r['Crime_against_person']
        property_offences = r['Property_offences']
        drug_offences = r['Drug_offences']
        public_order_offences = r['Public_order_offences']
        justice_procedures_offences = r['Justice_procedures_offences']
        other_offences = r['Other_offences']
        ambulance_response = r['Ambulance_response']

        new_compare = Compare(name, distance, time, suburb_1, suburb_2, suburb_3, suburb_4, suburb_5, population, population_density, overseas_rank, unemployment_rate,
                              one_br_flat, two_br_flat, three_br_flat, two_br_house, three_br_house, four_br_house, tram, bus, train, crime_against_person, property_offences, drug_offences, public_order_offences, justice_procedures_offences, other_offences, ambulance_response)

        db.session.add(new_compare)
        db.session.commit()

    return infos_schema.jsonify(new_compare)

# Create a lga
@app.route('/lga',  methods=['POST'])
def add_lga():
    country = request.json['Country']
    info = request.json['Info']
    suburb = request.json['Suburb']

    new_lga = Lga(country, info, suburb)

    db.session.add(new_lga)
    db.session.commit()

    return lga_schema.jsonify(new_lga)

# Create an event
@app.route('/addevent',  methods=['POST'])
def add_event():
    req = request.get_json()['all_events']
    for r in req:

        event_id = r['event_id']
        name_text = r['name_text']
        description_text = r['description_text']
        summary = r['summary']
        url = r['url']
        start_date = r['start_date']
        start_time = r['start_time']
        end_date = r['end_date']
        end_time = r['end_time']
        venue_id = r['venue_id']
        logo_original = r['logo_original']
        community = r['community']
        location = r['location']

        new_event = Event(event_id, name_text, description_text, summary, url, start_date,
                          start_time, end_date, end_time, venue_id, logo_original, community, location)

        db.session.add(new_event)
        db.session.commit()

    return events_schema.jsonify(new_event)


# Get All suburbs
@app.route('/suburb', methods=['GET'])
def get_suburbs():
    all_suburbs = Suburb.query.all()
    result = suburbs_schema.dump(all_suburbs)
    return jsonify(result.data)

# Get All lgas
@app.route('/lga', methods=['GET'])
def get_lgas():
    all_lgas = Lga.query.all()
    result = lgas_schema.dump(all_lgas)
    return jsonify(result.data)

# Get All Events
@app.route('/addevent', methods=['GET'])
def get_events():
    all_events = Event.query.all()
    result = events_schema.dump(all_events)
    return jsonify(result.data)


def readJsonFile(filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    final_filename = os.path.join(script_dir, filename)
    with open(final_filename, encoding="utf-8-sig") as json_file:
        return json.load(json_file)


#filename = readJsonFile(abs_file_path)


url_head = "https://www.eventbriteapi.com/v3/events/"
url_body = "/?expand=venue&token="
token = "CR32Z5HAAMMYMKZE6CAT"


def update_events_locations(events_dic):
    for x in events_dic:
        url = url_head + str(x['id']) + url_body + token
        response = requests.get(url).json()
        # response_dic = json.loads(response)
        # print(response['venue']['address']['localized_address_display'])
        location = response['venue']['address']['localized_address_display']
        x['location'] = location
        # print(x)
        # print('\n ')
    return events_dic


def event_filter_by_nationality(events, nationality):
    res = []
    for event in events:
        if event['community'] == nationality:
            res.append(event)
    return res


def getByNationality(filename, countryname):
    output = []

    for item in filename:
        if item["Country"] == countryname:
            output.append(item)

    return output


def get_header(item):
    out = item['LGA Name']
    return out


def lga_extractor(filename, key, param):
    for entry in filename:
        if entry[key] == param:
            return entry
    return {}


# Views urls

@app.route('/')
def index2():
    return render_template('index.html')


@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/profile-China')
def profile_china():
    return render_template('profile-China.html')


@app.route('/profile-India')
def profile_india():
    return render_template('profile-India.html')


@app.route('/profile-Iran')
def profile_iran():
    return render_template('profile-Iran.html')


@app.route('/events-default')
def suburb():
    return render_template('profile-noNationality-1.html')


@app.route('/lga/<name>', methods=['GET', 'POST'])
def lga(name):
    print("name clicked", name)
    output = Info.query.filter_by(Name=name).all()
    print("type:", type(output))
    print("type:", type(output[0]))

    return render_template('Suburb.html', lga=output[0])


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
    my_events = Event.query.filter_by(community="Chinese").all()
    return render_template('events-new.html', events=my_events)


@app.route('/events_iranian')
def events_iranian():
    my_events = Event.query.filter_by(community="Iranian").all()
    return render_template('events-new.html', events=my_events)


@app.route('/events_indian')
def events_indian():
    my_events = Event.query.filter_by(community="Indian").all()
    return render_template('events-new.html', events=my_events)


lga_name_lst = ["Boroondara", "Casey", "Greater Dandenong", "Manningham",
                "Melbourne", "Monash", "Whitehorse", "Whittlesea", "Wyndham"]


@app.route('/comparetwo')
def comparetwo():
    return render_template('comparetwo.html', lga_name=lga_name_lst)


@app.route('/success', methods=['GET', 'POST'])
def success():
    if request.method == "POST":
        lga_brand = request.form.get("cars", None)
        lga_brand2 = request.form.get("motors", None)
        if (lga_brand and lga_brand2) != None:
            rent = Compare.query.filter_by(Name=lga_brand).all()[0]
            rent2 = Compare.query.filter_by(Name=lga_brand2).all()[0]
            return render_template("comparetwo.html", c1=rent, c2=rent2, lga_name=lga_name_lst)
    return render_template("comparetwo.html")


@app.route('/learnmore')
def learn_more():
    return render_template('learnMore.html')


@app.route('/quiz-language')
def quiz_language():
    colour = "#007BFF"
    return render_template('quiz.html', colour=colour)


@app.route('/quiz-transport')
def quiz_transport():
    colour = "#28A745"
    return render_template('quiz.html', colour=colour)


@app.route('/quiz-sport')
def quiz_sport():
    colour = "#868E96"
    return render_template('quiz.html', colour=colour)


@app.route('/quiz-culture')
def quiz_culture():
    colour = "#DC3545"
    return render_template('quiz.html', colour=colour)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
