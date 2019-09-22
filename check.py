import mosspy
import os
import requests
from bs4 import BeautifulSoup as bs
from dotenv import load_dotenv
load_dotenv()

userid = os.environ['USER_ID']

def submitFiles(program_list, language):
	"""
	Get Moss Results Report URL
	"""
	m = mosspy.Moss(userid, language)
	for item in program_list:
		m.addFile(item)
	url = m.send()
	return url

def downloadReport(url):
	"""
	Download whole report locally including code diff links
	"""
	mosspy.download_report(url, "submission/report/", connections=8)


def extractInfo(url, files):
	"""
	Scrape the webpage for percentage match etc.
	"""
	res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
	html = bs(res.text, "lxml")

	for row in html.find_all('tr'):
		cols = row.find_all('td')
		cols = [x.text.strip() for x in cols]

	for item, file in zip(cols, files):
		percentage = item[len(file)+1:]

	print("Report URL : " + url)
	print(percentage + " code matched in " + str(files))
	print("Lines Matched : " + str(cols[-1]))

files = ['testfiles/test_python.py', 'testfiles/test_python2.py']
url = submitFiles(files, "Python")
extractInfo(url, files)