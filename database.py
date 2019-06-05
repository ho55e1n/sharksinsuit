from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from main import db, ma
from flask_marshmallow import Marshmallow
import json
import os


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
