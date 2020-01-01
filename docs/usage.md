# Usage

plagcheck provides the following class constructors

### check(files, lang, user_id)

* **Parameters** :
  - files : Program Files.
  - lang : The Programming Language.
  - output : Moss UserID.


**Demo**:
```python

"""Usage example"""
import os
import pprint
from plagcheck import plagcheck
from dotenv import load_dotenv
load_dotenv()

program_files = [
  "testfiles/test_python.py",
  "testfiles/test_python3.py",
  "testfiles/test_python2.py"
]

language = "python"
userid = os.environ["USER_ID"]


cheat = plagcheck.check(program_files, language, userid)

# cheat.addBaseCode("submission/a01.py")

cheat.submit()

print(cheat.getHomePage())
pprint.pprint(cheat.getResults())

```

### 1. submit()
**Parameters** : `None` <br>
**Return Type** : `None` <br>
**Description**: Submits the program on Moss.<br>
**Demo**:
```python

c.submit()

```

### 2. getHomePage()
**Parameters** : `None` <br>
**Return Type** : `String` <br>
**Description**: Returns the Moss Result HomePage<br>
**Demo**:
```python

c.getHomePage()

```

### 3. getResults()
**Parameters** : `None` <br>
**Return Type** : `List` <br>
**Description**: Returns the scraped data from Moss Results .<br>
**Demo**:
```python

c.getResults()
"""
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
"""

```