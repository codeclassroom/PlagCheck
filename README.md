# PlagCheck ✅

> Moss Results scraper with powerful insights & analysis 💡

![PyPI](https://img.shields.io/pypi/v/plagcheck?color=blue)
[![Build Status](https://travis-ci.org/codeclassroom/PlagCheck.svg?branch=master)](https://travis-ci.org/codeclassroom/PlagCheck)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/plagcheck)
[![Documentation Status](https://readthedocs.org/projects/plagcheck/badge/?version=latest)](https://plagcheck.readthedocs.io/en/latest/?badge=latest)
![PyPI - License](https://img.shields.io/pypi/l/plagcheck?color=orange)
![PyPI - Downloads](https://img.shields.io/pypi/dm/plagcheck?color=blue)


## Installation

Install using `pip` from PyPI

```bash
pip install plagcheck
```

or directly from GitHub if you cannot wait to test new features

```bash
pip install git+https://github.com/codeclassroom/PlagCheck.git
```

## Usage

```python

"""Usage example"""
import os
import pprint
from plagcheck.plagcheck import check, insights, share_scores

from dotenv import load_dotenv
load_dotenv()

language = "java"
userid = os.environ["USER_ID"]


moss = check(language, userid)

moss.addFilesByWildCard("testfiles/test_java*.java")

# or moss.addFile("testfiles/test_python.py")

moss.submit()

print(moss.getHomePage())

result = moss.getResults()

pprint.pprint(result)

# print potential distributor-culprit relationships
pprint.pprint(insights(result))
# print frequency of each shared solution
pprint.pprint(share_scores(result))

```

## Documentation

> [PlagCheck Documentation](https://plagcheck.readthedocs.io/en/latest/)


## Development

##### Prerequisites
- Python 3.6+
- virtualenv

1. Create virtual environment.
```bash
virtualenv -p python3 venv && cd venv && source bin/activate
```
2. Clone the repository.
```bash
git https://github.com/codeclassroom/PlagCheck.git
```
3. Install Dependencies.
```bash
pip install -r requirements-dev.txt
```
4. Run tests.
```bash
pytest plagcheck
```
5. Lint the project with
```bash
flake8 plagcheck --max-line-length=88 --ignore=F401
black --check --diff plagcheck
```

## 📝 Changelog

See the [CHANGELOG.md](CHANGELOG.md) file for details.


## Author

👥 **Bhupesh Varshney**

- Twitter: [@bhupeshimself](https://twitter.com/bhupeshimself)
- DEV: [bhupesh](https://dev.to/bhupesh)

[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 👋 Contributing

Please read the [CONTRIBUTING](CONTRIBUTING.md) guidelines for the process of submitting pull requests to us.


## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/vhsw"><img src="https://avatars3.githubusercontent.com/u/7099976?v=4" width="100px;" alt="Alexey Dubrov"/><br /><sub><b>Alexey Dubrov</b></sub></a><br /><a href="https://github.com/codeclassroom/PlagCheck/commits?author=vhsw" title="Code">💻</a> <a href="https://github.com/codeclassroom/PlagCheck/issues?q=author%3Avhsw" title="Bug reports">🐛</a> <a href="https://github.com/codeclassroom/PlagCheck/commits?author=vhsw" title="Tests">⚠️</a></td>
  </tr>
</table>

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
