"""Usage example"""
import os
import pprint
from plagcheck import plagcheck

program_files = ["testfiles/test_python.py", "testfiles/test_python3.py"]
language = "python"
userid = os.environ["USER_ID"]

url, results = plagcheck.check(program_files, language, userid)


print(url)
pprint.pprint(results)
