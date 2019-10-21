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