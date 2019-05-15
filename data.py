import os
import json
import requests


# with open('data.txt') as json_file:
#     data = json.load(json_file)
#
#
# print(json.dumps(data["all_suburbs"], indent=4))


# with open('Country_LGA_Suburb Ranked.txt') as json_file:
#     data = json.load(json_file)


def readJsonFile(filename):
        # get the dir path
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # join dir with filename
    final_filename = os.path.join(script_dir, filename)
    # open the file
    with open(final_filename, encoding="utf-8-sig") as json_file:
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


# input = readJsonFile('chinese_data.txt')['all_suburbs']


def lga_extractor(filename, key, param):
    for entry in filename:
        if entry[key] == param:
            return entry
    return {}


# print(input[0]['name'])

# print(lga_extractor(input, 'Camberwell'))

def get_header(item):
    out = item['LGA Name']
    return out


# data = readJsonFile("final_compareData.json.txt")['lga']
# #out = lga_extractor(data, 'LGA', 'Casey')['Tableau Embed Rent']
# print(json.dumps(data, indent=4))
# print(len(data))
# lga_final = readJsonFile("LGA_COMPARE_FINAL.json.txt")['lga']

# map_get_header = list(map(get_header, lga_final))
# print(map_get_header)


data2 = readJsonFile("ChineseEvents.json.txt")['events']

url_head = "https://www.eventbriteapi.com/v3/events/"
url_body = "/?expand=venue&token="
token = "CR32Z5HAAMMYMKZE6CAT"


def update_events_locations(events_dic, nationality):
    for x in events_dic:
        url = url_head + str(x['id']) + url_body + token
        response = requests.get(url).json()
        # response_dic = json.loads(response)
        # print(response['venue']['address']['localized_address_display'])
        if response.get('status_code') == 403:
            x['location'] = "Need to Register"
        else:
            location = response['venue']['address']['localized_address_display']
            x['location'] = location
        print(x)
        print('\n ')
    with open('event_updated_' + nationality + '.txt', 'w') as outfile:
        json.dump(events_dic, outfile, indent=4)


# url = url_head + '61217263483' + url_body + token
# response = requests.get(url).json()
# print(response.get('status_code') == 403)
# update_events_locations(data2, 'chinese')

# entry = {'location': 'melbourne'}
# data2['location'] = 'melbourne'
# print(type(data2))
# print(type(json.dumps(data2, indent=4)))
# print(json.dumps(data2, indent=4))


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

# with open('LGAFINAL.txt') as jsonFile:
#     jsonStr = jsonFile.read()

# jsonData = json.loads(jsonStr)

# print(json.dumps(jsonData, indent=4))

# print(os.path.dirname(os.path.abspath(__file__)))

events = readJsonFile("event_updated_chinese.txt")
print(events[0]['logo'])
