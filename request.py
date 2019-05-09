import requests
import json
import time

url = "https://www.eventbriteapi.com/v3/events/search/?sort_by=date&location.address=victoria%2Caustralia&token=CR32Z5HAAMMYMKZE6CAT&page="
# response = requests.get(url+"1").json()
# #print(type(response.content))
# #response_json = (response.content)
# print(json.dumps(response, indent=4))
#
# with open('output.txt', 'w') as outfile:
#     json.dump(response, outfile, indent=4)

for i in range(200, 201):
    response = requests.get(url + str(i)).json()
    with open('event_page' + str(i) + '.txt', 'w') as outfile:
        json.dump(response, outfile, indent=4)
        time.sleep(2)
