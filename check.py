import mosspy
import os
import requests
import datetime
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


def getFormattedDate(date_time):
	#Thu Oct 3 00:16:17 PDT 2019
	#timezone is sill PDT, need to change
	date = date_time[0:18] + " " + date_time[23:27]
	date_time_obj = datetime.datetime.strptime(
		str(date), '%c')
	date = str(date_time_obj.date())
	time = str(date_time_obj.time())
	return date, time


def extractInfo(url, files):
	"""
	Scrape the webpage for percentage match etc.
	"""
	cols = []
	filenames = []

	res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
	html = bs(res.text, "lxml")

	date_time = html.find_all('p')[0]
	date_time = " ".join(date_time.text.split())
	# get the results table
	table = html.find_all('table')[0]

	for row in table.find_all('tr'):
		columns = row.find_all('td')
		for filename in columns:
			column_marker = 0
			if column_marker <=1:
				cols.append(filename.text.strip())
			column_marker += 1
	# get line 
	# for link in columns:
	# 	if link.a != None:
	# 		result_link = link.a["href"]
	# 		cols.append(result_link)

	for item, file in zip(cols, files):
		percentage = item[len(file)+2:len(item)-2]
		filenames.append(item[0:len(file)])

	date, time = getFormattedDate(date_time)
	result_dict = dict(
		file1 = filenames[0], 
		file2 = filenames[1], 
		percentage = int(percentage),
		url = url,
		date = date,
		time = time
	)

	results.append(result_dict)
	print(results)
	
	#redundant data
	print("Lines Matched : " + str(cols[-1]))
	
files = ['testfiles/test_python.py', 'testfiles/test_python2.py']

url = submitFiles(files, "Python")
extractInfo(url, files)