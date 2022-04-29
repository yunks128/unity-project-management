import requests
import click
from requests.auth import HTTPBasicAuth
import csv
import json


repos = [444566727,429213490,429766212,429216825,429538396,429541482,446539903,449776091,446987126,457504758]
zenhub_url = "https://api.zenhub.com"

github_org = "unity-sds"
release_report = "Z2lkOi8vcmFwdG9yL1JlbGVhc2UvNzA0MjQ"

@click.group()
def reports():
    pass

@reports.command(short_help="A command to generate the epics included in a specific release. It will contain the status, title, componenet, description, and link to underlying github issue.")
@click.option('--release', prompt='Release ID', default="Z2lkOi8vcmFwdG9yL1JlbGVhc2UvNzA0MjQ",
              help='Release ID - found in the url of an example releaes report: https://app.zenhub.com/workspaces/unity-workspace-61d4b6a48ed26b001d7d184a/reports/release?release={RELEASE REPORT}')
def release_report(release):
    epics = []
    user_env = read_env()
    rgen = ReportGenerator(user_env['zenhubkey'], user_env['github_user'], user_env['github_key'])
    zh_release_issues = rgen.get_zenhub_release_issues(release)
    for issue in zh_release_issues:
        #{'repo_id': 449776091, 'issue_number': 33}
        zh_issue = rgen.get_zenhub_issue_data(issue['repo_id'],issue['issue_number'])
        if zh_issue['is_epic'] == True:
            repository = rgen.get_github_repo_from_zenhub_repo_id(issue['repo_id'])
            print(repository)
            gh_epic = rgen.get_github_issue("unity-sds", repository['name'], issue['issue_number'])
            gh_epic['repo_name'] = repository['name']
            epics.append(gh_epic)

    with open('zh_report.csv', 'w', newline='') as csvfile:
        csvw = csv.writer(csvfile)
        csvw.writerow(["status", "title", "componenet", "description", "link"])
        for epic in epics:
            csvw.writerow([epic["state"], epic["title"], epic["repo_name"], epic["body"], epic["url"]])

def read_env():
    f = open('report.env')
    return json.load(f)


class ReportGenerator():

    repo_map = {}

    def __init__(self, zhkey, ghuser, ghkey, ghorg="unity-sds"):
        self.zenhubkey = zhkey
        self.github_user = ghuser
        self.github_key = ghkey
        self.github_org = ghorg

    def get_github_repo_from_zenhub_repo_id(self, repo_id):
        gh_repo = self.repo_map.get(repo_id, None)
        if gh_repo == None:
            print("cache miss, getting repo info from github")
            gh_repo = self.get_github_repo_data(repo_id)
            self.repo_map[repo_id] = gh_repo
        return gh_repo

    def get_milestone(self, epic):
        if epic["milestone"] is not None:
            return epic["milestone"]["description"]

    #Given a relaes id, get the release report for it
    def get_zenhub_release_issues(self, release_id):
        url = zenhub_url + "/p1/reports/release/{0}/issues".format(release_id)
        print("Fetching {}".format(url))
        resp = requests.get(url, headers={"X-Authentication-Token": self.zenhubkey, "Content-Type": "application/json"}).json()
        return resp


    # Given a repo id, get the epics for that repo from zenhub
    def get_zenhub_epics_by_repo_id(self, repo_id):
        url = zenhub_url + "/p1/repositories/{0}/epics".format(repo_id)
        print("Fetching {}".format(url))
        resp = requests.get(url, headers={"X-Authentication-Token": self.zenhubkey, "Content-Type": "application/json"}).json()
        return resp

    def get_zenhub_issue_data(self, repo, issue):
        url = zenhub_url + "/p1/repositories/{0}/issues/{1}".format(repo, issue)
        print("Fetching {}".format(url))
        resp = requests.get(url, headers={"X-Authentication-Token": self.zenhubkey, "Content-Type": "application/json"}).json()
        return resp

    def get_zenhub_epic_data(self, repo, epic):
        url = zenhub_url + "/p1/repositories/{0}/epics/{1}".format(repo, epic)
        print("Fetching {}".format(url))
        resp = requests.get(url, headers={"X-Authentication-Token": self.zenhubkey, "Content-Type": "application/json"}).json()
        return resp

    ##################
    # GITHUB Accesses
    ##################
    #Get data (e.g. labels, description) from a github issue
    def get_github_issue(self, org, repo_name, issue):
        url = "https://api.github.com/repos/{0}/{1}/issues/{2}".format(org, repo_name, issue)
        print("Fetching {}".format(url))
        issue_json = requests.get(url, auth=HTTPBasicAuth(self.github_user, self.github_key)).json()
        return issue_json

    # given a repos ID, get the repo data from github
    # This API is not documented publicly...
    def get_github_repo_data(self, repo_id):
        url = "https://api.github.com/repositories/{0}".format(repo_id)
        repo = requests.get(url, auth=HTTPBasicAuth(self.github_user, self.github_key)).json()
        return repo

cli = click.CommandCollection(sources=[reports])

if __name__ == '__main__':
    cli()
# if __name__ == '__main__':
#     release_report()
