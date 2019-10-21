import os
import PlagCheck.check as plagcheck
from dotenv import load_dotenv

load_dotenv()

userid = os.environ["USER_ID"]

program_files = ["testfiles/test_python.py", "testfiles/test_python3.py"]
language = "Python"

url, results = plagcheck.check(program_files, language, userid)


print(url)
print(results)
