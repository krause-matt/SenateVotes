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
