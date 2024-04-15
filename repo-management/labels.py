import os
import requests

org = "unity-sds"
gh = "https://api.github.com/"

# Token must have repo management capabilities
ghtoken = os.environ.get('GITHUB_TOKEN', None)
if ghtoken is None:
    print("A github token is required to update the repositories.")


labels = [
     {
        "name":"dependency",
        "description":"Ticket designating a dependency",
        "color":"5319E7"
     },
     {
        "name":"blocked",
        "description":"Label blocked issues to raise awareness",
        "color":"B60205",
     },
     {
        "name":"U-ADS",
        "color":"006B75"
     },
     {
        "name":"U-AS",
        "color":"006B75"
     },
     {
        "name":"U-CS",
        "color":"006B75"
     },
     {
        "name":"U-DS",
        "color":"006B75"
     },
     {
        "name":"U-SPS",
        "color":"006B75"
     },
     {
        "name":"U-UIUX",
        "color":"006B75"
     },
     {
        "name":"PSE",
        "color":"006B75"
     },
     {
        "name":"Unity-On-Demand",
        "color":"006B75"
     },
]

# service area
#label color: 006B75
# dependency
# color 5319E7
# blocked
# color: B60205
def get_labels(repo):
    print("Getting labels for " + repo)
    url = gh +"repos/" + org + "/" + repo + "/labels"
    print(url)
    headers = {"Authorization": "Bearer " + ghtoken}
    labels = requests.get(url, headers=headers).json()
    return [x['name'] for x in labels]


def add_label(label):
    #print("adding label " + str(label) )
    headers = {"Authorization": "Bearer " + ghtoken, "Accept": "application/vnd.github+json", 'User-Agent': 'mike-gangl', 'X-GitHub-Api-Version': '2022-11-28' }
    print(headers)
    print(label)
    url = gh +"repos/" + org + "/" + repo + "/labels"

    response = requests.post(url, headers=headers, json=label)
    print(response)


repository_list = open('repositories.txt')
for repo in repository_list:
    repo = repo.strip()
    print( "Processing labels for " + repo)
    repo_labels = get_labels(repo)
    print(repo_labels)
    for label in labels:
        if label['name'] not in repo_labels:
            add_label(label)
repository_list.close()
