# Usage

plagcheck provides the following classes & methods:

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
**Description**: Returns the Moss Result HomePage URL<br>
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

```

*getResults()* returns the following list of dictionaries:
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
Each dict item contains the following items:

- **file1** & **file2** : 
The pair of file names that have similar code.

- **percentage** : 
It is the the percentage of the code in one file considered to match code in the other file.

- **lines_matched** : 
  Lines Matched is approximately the number of lines of code that matched between 2 given files.

  For example :
  If ***lines_matched* is [['88-99','119-131']]**
  
  Then the line numbers 88-99 of *file1* matched with lines 119-131 of *file2*.

  lines_matched is a list of lists indicating all line number matches between 2 code files.


> For both measures(*lines_matched* & *percentage*), higher numbers mean more code matches.

### 4. addFilesByWildCard()
**Parameters** : `String` <br>
**Return Type** : `None` <br>
**Description**: Add multiple files.<br>
**Demo**:
```python

c.addFilesByWildCard("testfiles/test_python*.py")
# This will add all the files having names like, test_python2, test_python5 etc.

```

### 5. addFile()
**Parameters** : `String` <br>
**Return Type** : `None` <br>
**Description**: Add a single file for submission.<br>
**Demo**:
```python

c.addFile("testfiles/test_python.py")

```

### 6. addBaseCode()
**Parameters** : `String` <br>
**Return Type** : `None` <br>
**Description**: Add an allowed code file which is use by Moss to ignore results matching with this file<br>
**Demo**:
```python

c.addBaseCode("/base.py")

```

- Moss normally reports all code
that matches in pairs of files. When a base file is supplied,
program code that also appears in the base file is not counted in matches.
- A typical base file will include, for example, the instructor-supplied
code for an assignment. Multiple Base files are allowed.
- You should use a base file if it is convenient; base files improve results, but are not usually necessary for obtaining useful information.

<hr>

### share_scores()
**Parameters** : `Moss Results`(returned by `getResults()`) <br>
**Return Type** : `Dict` <br>
**Description**: Share Score is a utility which returns frequency of every individual file.<br>
**Demo**:
```python

print(share_scores(moss_data))

# Will return
"""
{'testfiles/test_python.py': 2,
 'testfiles/test_python2.py': 2,
 'testfiles/test_python3.py': 2}
"""
```
Share Score is basically the frequency of each file appearing in Moss Results.
i.e Higher the frequency, the more is that solution "shared" by different files.

### insights()
**Parameters** : `Moss Results`(returned by `getResults()`) <br>
**Return Type** : `Dict` <br>
**Description**: See [Insights](/insights).<br>
**Demo**:
```python

print(insights(moss_data))

```