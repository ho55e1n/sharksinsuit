import requests
import json
import time
import pandas
import os

token = 'API_KEYS_GOES_HERE'
body_url = 'https://www.eventbriteapi.com/v3/events/search/?sort_by=date&location.address=victoria%2Caustralia&token='
navigation = '&page='
url = body_url + token + navigation


# This method fetches all the events in victoria and create text files per page on root folder
for i in range(1, 201):
    response = requests.get(url + str(i)).json()
    with open('event_page' + str(i) + '.txt', 'w') as outfile:
        json.dump(response, outfile, indent=4)
        time.sleep(0.5)


# Reading from filtered events file and convert it to json
def readJsonFile(filename):
        # get the dir path
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # join dir with filename
    final_filename = os.path.join(script_dir, filename)
    # open the file
    with open(final_filename, encoding="utf-8-sig") as json_file:
        return json.load(json_file)


url_head = "https://www.eventbriteapi.com/v3/events/"
url_body = "/?expand=venue&token="
token = "API_KEYS_GOES_HERE"

# Take the filtered events and call the api to fetch location and extra information from eventbrite API


def update_events_locations(events_dic):
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
    with open('events_updated' + '.txt', 'w') as outfile:
        json.dump(events_dic, outfile, indent=4)


new_events = readJsonFile("events.json")
update_events_locations(new_events)
