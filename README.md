# PlagCheck ✅
The MOSS interface package for CodeClassroom

### Installation 🔮

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


### Usage

Import the `check` method from *PlagCheck*.

```python
import os
import PlagCheck.check as plagcheck
from dotenv import load_dotenv
load_dotenv()

userid = os.environ['USER_ID']

program_files = ['testfiles/test_python.py', 'testfiles/test_python3.py']
language = "Python"

p = plagcheck.check(program_files, language, userid)

results = p.getResults()
url = p.getURL()
date, time = p.getDateTime()

print(url)
print(results)

print(date)
print(time)
```

Read [Documentation](https://github.com/codeclassroom/PlagCheck/blob/master/docs/docs.md).


### TODO:

Fetch the URL and gather following results:

- [x] Percentage of Code Matches
- [x] Number of Lines Matched
- [x] URL itself
- [ ] Lines Matched
- [x] Return a list of dictionaries containing:
    ```json
    [
      {
        "file1":"filename1.py",
        "file2":"filename2.py",
        "percentage": 34,
        "no_of_lines_matched": 3,
        "lines_matched":[["2-3", "10-11"]]
      },
    ....
    ]
    ```


### Author

👥 **Bhupesh Varshney**

- Twitter: [@bhupeshimself](https://twitter.com/bhupeshimself)
- DEV: [bhupesh](https://dev.to/bhupesh)
