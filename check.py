import mosspy
import os
from dotenv import load_dotenv
load_dotenv()

userid = os.environ['USER_ID']

# Get Moss Results Report URL
def detectCheat(program_list, language):
	m = mosspy.Moss(userid, language)
	for item in program_list:
		m.addFile(item)
	url = m.send()
	return url

# Download whole report locally including code diff links
def downloadReport(url):
	mosspy.download_report(url, "submission/report/", connections=8)
