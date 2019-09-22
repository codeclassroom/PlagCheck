import mosspy
import os
import requests
from bs4 import BeautifulSoup as bs
from dotenv import load_dotenv
load_dotenv()

userid = os.environ['USER_ID']

# Get Moss Results Report URL
def submitFiles(program_list, language):
	m = mosspy.Moss(userid, language)
	for item in program_list:
		m.addFile(item)
	url = m.send()
	return url

# Download whole report locally including code diff links
def downloadReport(url):
	mosspy.download_report(url, "submission/report/", connections=8)

# Scrape the webpage for percentage match etc.
def extractInfo(url):
	res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
	html = bs(res.text, "lxml")

	for row in html.find_all('tr'):
		cols = row.find_all('td')
		cols = [x.text.strip() for x in cols]
		print(cols)


url = submitFiles(['test_python.py', 'test_python2.py'], "Python")
print(url)
extractInfo(url)