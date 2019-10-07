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

def getLineNumbers(diff_link):
	"""
	Get Line Numbers which are same
	"""
	line_no_set = set()
	page_name = diff_link.split('/')[5].split('.')[0]
	top_frame_name = "-top.html"
	result_link = "http://moss.stanford.edu/results/"
	result_id = diff_link.split('/')[4] + "/"
	result_page = result_link + result_id + page_name + top_frame_name
	res = requests.get(result_page, headers={'User-Agent': 'Mozilla/5.0'})
	html = bs(res.text, "lxml")
	table = html.find_all('table')[0]
	#print(table)

	for row in table.find_all('tr'):
		columns = row.find_all('td')
		for filename in columns:
			if filename.text.strip() != '':
				line_no_set.add(filename.text.strip())
	
	return list(line_no_set)


def getFormattedDate(date_time):
	"""
	Ex : Thu Oct 3 00:16:17 PDT 2019
	timezone is sill PDT, need to change
	"""
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
	diff_link = []

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

		for link in columns:
			if link.a != None:
				result_link = link.a["href"]
				diff_link.append(result_link)

	if len(diff_link) == 0:
		# Means the table is empty
		print("No Matches")
	elif diff_link[0] == diff_link[1]:
		line_numbers = getLineNumbers(diff_link[0])

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
		time = time,
		lines_matched = line_numbers
	)

	results.append(result_dict)
	print(results)

	#redundant data
	print("Lines Matched : " + str(cols[-1]))
	
files = ['testfiles/test_java.java', 'testfiles/test_java2.java']

url = submitFiles(files, "Java")
print(url)
extractInfo(url, files)
# diff = "http://moss.stanford.edu/results/835218475/match0.html"
# getLineNumbers(diff)