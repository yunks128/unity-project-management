# Zenhub reports

Zenhub is great. but sometimes we need a different or custom report or an export of it for some reason. This tool set allows us to do this.


## Install

checkout the repository and cd into the zenhub-reports subdirectory. Python 3.X is required.

## Requirements

```
pip install -r requirements.txt
```

This will install the `click` and `requests` modules.


## Running

1. first, copy the `report.env.sample` file locally to `report.env`
2. Update the values within the report.env file- it will need a zenhub access key, a github username, and a github personal access token (PAT) to generate the reports.
3. Run the command!

### Overview

```
python zh-reports.py
Usage: zh-reports.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  release-report  A command to generate the epics included in a specific
                  release. It will contain the status, title, componenet,
                  description, and link to underlying github issue.
```
