import os
import json


# with open('data.txt') as json_file:
#     data = json.load(json_file)
#
#
# print(json.dumps(data["all_suburbs"], indent=4))


# with open('Country_LGA_Suburb Ranked.txt') as json_file:
#     data = json.load(json_file)


def readJsonFile(filename):
    with open(filename) as json_file:
        return json.load(json_file)
#
#
# data = readJsonFile(abs_file_path)
#
#
# def getByNationality(filename, countryname):
#     output = []
#
#     for item in filename:
#         if item["Country"] == countryname:
#             item.pop("Country")
#             # item.pop("Info")
#             output.append(item)
#
#     return output
#
#
# output = getByNationality(data, "Iran")
# print(json.dumps(output[0:6], indent=4))
# print(len(output))


# input = readJsonFile('data.txt')['all_suburbs']


def lga_extractor(filename, param):
    for entry in filename:
        if entry['name'] == param:
            return entry
    return {}


# print(input[0]['name'])

# print(lga_extractor(input, 'Camberwell'))

script_dir = os.path.dirname(__file__)
rel_path = "events.txt"
abs_file_path = os.path.join(script_dir, rel_path)

data = readJsonFile(abs_file_path)['events'][0]['logo']['url']
print(json.dumps(data, indent=4))

# Grab text
# data = readJsonFile(abs_file_path)['events'][0]['name']['text']
# Grab desciption
# data = readJsonFile(abs_file_path)['events'][0]['description']['text']
# Grab url
# data = readJsonFile(abs_file_path)['events'][0]['url']
# Grab start day
# data = readJsonFile(abs_file_path)['events'][0]['start']['local'][0:10]
# Grab start time
# data = readJsonFile(abs_file_path)['events'][0]['start']['local'][11:17]
# Grab logo image
# data = readJsonFile(abs_file_path)['events'][0]['logo']['url']
