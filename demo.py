"""Usage example"""
import os
import pprint
from plagcheck import plagcheck
import time
from dotenv import load_dotenv
load_dotenv()

program_files = ["testfiles/test_python.py", "testfiles/test_python3.py"]
language = "python"
userid = os.environ["USER_ID"]


cheat = plagcheck.check(program_files, language, userid)

cheat.submit()

print(cheat.getHomePage())
pprint.pprint(cheat.getResults())
