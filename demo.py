import os
import PlagCheck.check as plagcheck

userid = os.environ['USER_ID']

program_files = ['testfiles/test_python.py', 'testfiles/test_python3.py']
language = "Python"

p = plagcheck.check(program_files, language, userid)

results, url = p.getResults()

print(url)
print(results)