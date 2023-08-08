<!-- Header block for project -->
<hr>

<div align="center">

![logo](https://user-images.githubusercontent.com/3129134/163255685-857aa780-880f-4c09-b08c-4b53bf4af54d.png)

<h1 align="center">Standards Compliance Leaderboard</h1>
<!-- ☝️ Replace with your repo name ☝️ -->

</div>

<pre align="center">Tool to generate a Markdown table of SLIM standards compliance.</pre>
<!-- ☝️ Replace with a single sentence describing the purpose of your repo / proj ☝️ -->

<!-- Header block for project -->

[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](code_of_conduct.md) [![SLIM](https://img.shields.io/badge/Best%20Practices%20from-SLIM-blue)](https://nasa-ammos.github.io/slim/)
<!-- ☝️ Add badges via: https://shields.io e.g. ![](https://img.shields.io/github/your_chosen_action/your_org/your_repo) ☝️ -->

This repository serves to create a leaderboard table for the Unity project, representing the compliance status of [SLIM best practices](https://nasa-ammos.github.io/slim/) and standards across Unity repositories.

## Features

* Script to query Unity repositories and create a markdown table showcasing SLIM standards compliance, sorted by leader, printed to standard out.
* Actual, generated compliance leaderboard table.
* API jittering to prevent too many fast requests to GitHub at once
* Logging to share the status of repository compliance as the script runs
  
## Contents

* [Quick Start](#quick-start)
* [Changelog](#changelog)
* [FAQ](#frequently-asked-questions-faq)
* [Contributing Guide](#contributing)
* [License](#license)
* [Support](#support)

## Quick Start

Use this quick start guide to generate a fresh leaderboard table. 

### Run Instructions

Requirements: 
* Python 3
* `requests` module

Setup:
- Generate a GitHub personal access token and replace the string `TOKEN_GOES_HERE` with the value of your token

To generate a fresh leaderboard markdown table (printed to `stdout`), run the following command:

```
python leaderboard.py
```

You'll see an output similar to the contents of [leaderboard.md](leaderboard.md)

How to interpret the leaderboard contents:
- A ✅ indicates successful compliance, where as a ❌ indicates not fully compliant
- Most checks verify whether files within your repository that should exist, do in fact exist. Some checks are more specialized, such as:
  - "README" - checks if your README conforms to the [SLIM standard README](https://nasa-ammos.github.io/slim/docs/guides/documentation/readme/)
  - "Dev/User Documentation" check for links to be present in your README that point to specific Dev or User docs - this is part of the SLIM standard README

## Changelog

See our root [CHANGELOG.md](../CHANGELOG.md) for a history of our changes.

## Frequently Asked Questions (FAQ)

None. Please post a PR to ask a question.

## Contributing

Interested in contributing to our project? Please see our: [CONTRIBUTING.md](../CONTRIBUTING.md)

## License

See our: [LICENSE](../LICENSE)

## Support

Key points of contact are: [@riverma](https://github.com/riverma)
