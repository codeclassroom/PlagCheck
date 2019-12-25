"""Usage example"""
import os
import pprint
from plagcheck import plagcheck

from dotenv import load_dotenv
load_dotenv()

language = "java"
userid = os.environ["USER_ID"]


moss = plagcheck.check(language, userid)

moss.addFilesByWildCard("testfiles/test_java*.java")

# or moss.addFile("testfiles/test_python.py")

moss.submit()

print(moss.getHomePage())
pprint.pprint(moss.getResults())
pprint.pprint(moss.getShareScores())
pprint.pprint(moss.getDistributors())
pprint.pprint(moss.getCulprits())