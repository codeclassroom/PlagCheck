"""Usage example"""
import os
import pprint
from plagcheck import plagcheck

from dotenv import load_dotenv
load_dotenv()

language = "python"
userid = os.environ["USER_ID"]


moss = plagcheck.check(language, userid)

moss.addFilesByWildCard("testfiles/test_python*.py")

# or moss.addFile("testfiles/test_python.py")

moss.submit()

print(moss.getHomePage())
pprint.pprint(moss.getResults())
#pprint.pprint(moss.getShareScores()