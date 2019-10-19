import os
from PlagCheck.check import check

userid = os.environ['USER_ID']

program_files = ['testfiles/test_python.py', 'testfiles/test_python3.py']
language = "Python"

results, url = check(program_files, language, userid)
print(url)
print(results)