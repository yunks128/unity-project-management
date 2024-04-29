import os
import requests

org = "unity-sds"
gh = "https://api.github.com/"
ignore = ["unity-project-management", "issue-triage", "application-development-lifecycle", "unity-repo-template", "sounder-sips-application", "sounder-sips-chirp-workflows", "unity-sps-workflows", "unity-sps-prototype","unity-sps-register_job", "unity-sps-api", "unity-sps-prototype-fork", "unity-sps-on-demand-api","unity-cs-sps-demo", "unity-jobs-ui",  "ui-ux", "unity-on-demand-api", "unity-on-demand-cloudformation" ,"hysds_ui_with_auth"]


# Token must have repo management capabilities
ghtoken = os.environ.get('GITHUB_TOKEN', None)
if ghtoken is None:
    print("A github token is required to update the repositories.")


# service area
#label color: 006B75
# dependency
# color 5319E7
# blocked
# color: B60205
def get_latest_release(repo):
    url = gh +"repos/" + org + "/" + repo + "/releases/latest"
    headers = {"Authorization": "Bearer " + ghtoken}
    latest = requests.get(url, headers=headers).json()
    if "name" not in latest:
      return "N/A", "N/A", "N/A"
    return latest['name'], latest['tag_name'], latest['published_at']


repository_list = open('repositories.txt')
for repo in repository_list:
    repo = repo.strip()
    if repo not in ignore:
      repo_release, repo_tag, release_date  = get_latest_release(repo)
      print(repo + ", " + repo_release+ ", " + repo_tag + ", " + release_date)
repository_list.close()
