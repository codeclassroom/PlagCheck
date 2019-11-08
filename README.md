# PlagCheck ✅

![PyPI](https://img.shields.io/pypi/v/plagcheck?color=blue)
[![Build Status](https://travis-ci.org/codeclassroom/PlagCheck.svg?branch=master)](https://travis-ci.org/codeclassroom/PlagCheck)
[![GitHub license](https://img.shields.io/github/license/codeclassroom/PlagCheck)](https://github.com/codeclassroom/CodeRunner/blob/master/LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/codeclassroom/PlagCheck?color=blueviolet)](https://github.com/codeclassroom/CodeRunner/issues)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-orange.svg)](http://makeapullrequest.com)

> A Powerful [Moss](http://theory.stanford.edu/~aiken/moss/) results scrapper.

## Installation 🔮

1. Create virtual environment.

    **Linux/MacOS**

    ```bash
    virtualenv -p python3 venv && cd venv && source bin/activate
    ```

    **Windows**
    (*PowerShell*)

    ```cmd
    py -m venv venv; .\venv\Scripts\activate;
    ```

2. Clone the repository.

    ```bash
    git clone https://github.com/codeclassroom/PlagCheck.git
    ```

3. Install dependencies.

    ```bash
    pip install -r requirements.txt
    ```

4. Set-up virtual environment variables.
    1. Create a file named `.env` in the root directory & add the following contents.

        ```text
        USER_ID = 'moss-user-id'
        ```

    2. For `USER_ID` read instructions on [Moss](http://theory.stanford.edu/~aiken/moss/).

5. Run `demo.py` for demo.

## Usage

Install the package.

```bash
pip install plagcheck
```

```python
"""Usage example"""
import os
import pprint
import plagcheck
from dotenv import load_dotenv
load_dotenv()

program_files = ["testfiles/test_python.py", "testfiles/test_python3.py"]
language = "python"
userid = os.environ["USER_ID"]

url, results = plagcheck.check(program_files, language, userid)


print(url)
pprint.pprint(results)

```

Read [Documentation](https://github.com/codeclassroom/PlagCheck/blob/master/docs/docs.md).

## Author

👥 **Bhupesh Varshney**

- Twitter: [@bhupeshimself](https://twitter.com/bhupeshimself)
- DEV: [bhupesh](https://dev.to/bhupesh)

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
