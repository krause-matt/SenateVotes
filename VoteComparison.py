import requests
import json
#import pprint

headers = {'X-API-Key': 'fyrqYQVFxVQIx0HKc84LV5tmeFqAgHwoPuf8k5o0',}

#change congress and session numbers to specify correct year
url = "https://api.propublica.org/congress/v1/114/senate/sessions/1/votes/"

#compare each vote for the selected senate session
for i in range(1,314):
    json_response = requests.get(url + str(i) + ".json", headers = headers)
    data = json.loads(json_response.text)
    for x in data["results"]["votes"]["vote"]["positions"]:
        if x["name"] == "Bernard Sanders":
            sanders_vote = x["vote_position"]
        elif x["name"] == "Elizabeth Warren":
            warren_vote = x["vote_position"]
    if sanders_vote == warren_vote:
        print("Vote number : " + str(i) + " -- no difference.")
    else:
        if sanders_vote != "Not Voting" and warren_vote != "Not Voting":
            print("Vote number : " + str(i) + " -- SANDERS = " + sanders_vote.upper() + ", WARREN = " + warren_vote.upper())
        else:
            print("Vote number : " + str(i) + " -- someone not voting.")
            
"""
for i in range(1,20):
    json_response = requests.get(url + str(i) + ".json", headers = headers)
    data = json.loads(json_response.text)
    for x in data["results"]["votes"]["vote"]["bill"]:
        if x == "title":
            print(i)
            for y in data["results"]["votes"]["vote"]["bill"]["title"]:
                print(y, end="")

"""
"""
for i in range(3,4):
    json_response = requests.get(url + str(i) + ".json", headers = headers)
    data = json.loads(json_response.text)
    sponsor = ""
    description = ""
    for x in data["results"]["votes"]["vote"]["amendment"]["sponsor"]:
        sponsor = sponsor + x
    for x in data["results"]["votes"]["vote"]["description"]:
        description = description + x
    print(sponsor)
    print(description)
"""
"""
for i in range(1,340):
    json_response = requests.get(url + str(i) + ".json", headers = headers)
    data = json.loads(json_response.text)
    sponsor = ""
    description = ""
    print(str(i))
    if not data["results"]["votes"]["vote"]["amendment"]:
        pass
    else:
        if not data["results"]["votes"]["vote"]["amendment"]["sponsor"]:
            pass
        else:
            for y in data["results"]["votes"]["vote"]["amendment"]["sponsor"]:
                sponsor = sponsor + y
    if sponsor == "Bernard Sanders":
        for z in data["results"]["votes"]["vote"]["description"]:
            description = description + z
        print("Vote " + str(i) + " : Bernie Amendment = " + description)

"""
"""
for i in range(243,244):
    json_response = requests.get(url + str(i) + ".json", headers = headers)
    data = json.loads(json_response.text)
    print(data)
"""
