"""Usage example"""
import os
import pprint
from plagcheck import plagcheck
from dotenv import load_dotenv
load_dotenv()

program_files = [
	"testfiles/test_python.py",
	"testfiles/test_python3.py",
	"testfiles/test_python2.py"
]

# program_files = [
# "submission/Q1-Animesh.vb",
# "submission/Q1-Priyankan.vb",
# ]
language = "python"
userid = os.environ["USER_ID"]


moss = plagcheck.check(program_files, language, userid)

# cheat.addBaseCode("submission/a01.py")
# cheat.addBaseCode("submission/test_student.py")
moss.submit()

print(moss.getHomePage())
pprint.pprint(moss.getResults())
