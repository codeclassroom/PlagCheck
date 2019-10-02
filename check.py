import mosspy
import os
import requests
from bs4 import BeautifulSoup as bs
from dotenv import load_dotenv
load_dotenv()

userid = os.environ['USER_ID']

results = []

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

def getLineNumbers():
	pass

def extractInfo(url, files):
	"""
	Scrape the webpage for percentage match etc.
	"""
	res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
	html = bs(res.text, "lxml")

	date_time = html.find_all('p')[0]

	# get the results table
	table = html.find_all('table')[0]
	#print(table)
	for row in table.find_all('tr'):
		#column_marker = 0
		columns = row.find_all('td')
		cols = [filename.text.strip() for filename in columns]
		for link in columns:
			if link.a != None:
				result_link = link.a["href"]
				cols.append(result_link)

	print(cols)
	
	#its buggy need to fix
	for item, file in zip(cols, files):
		percentage = item[len(file)+1:]

	print("Report URL : " + url)
	print(percentage + " code matched in " + str(files))
	print("Lines Matched : " + str(cols[-1]))
	print("Date : " + date_time.text.strip())

files = ['testfiles/test_python.py', 'testfiles/test_python2.py']

url = submitFiles(files, "Python")
extractInfo(url, files)