# Repo Management Scripts

## Identifying Repositories

Many ops across repos need a list of repositories to work from. To create a list, simply run the following command:

```
curl -L   -H "Accept: application/vnd.github+json"    -H "X-GitHub-Api-Version: 2022-11-28"   https://api.github.com/orgs/unity-sds/repos?per_page=100 | jq -r .[].name
```

or using the gh app:

```
gh repo list unity-sds -L 100 --json name --visibility public --no-archived | jq -r ".[].name"
```


## Executing Commands

### latest releases

```
python latest-release.py > 1.0.0-prototype-manifest.csv
```


