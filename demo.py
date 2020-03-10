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
