import os
import re
import datetime
import requests
import mosspy
from bs4 import BeautifulSoup as bs
from dotenv import load_dotenv
load_dotenv()


class check:
	results = []

	def __init__(self, program_files, lang, user_id):
		self.user_id = user_id
		self.lang = lang
		self. program_files = program_files
		self.results = []

	def submitFiles(self):
		"""
		Get Moss Results Report URL
		"""
		m = mosspy.Moss(self.user_id, self.lang)
		for item in self.program_files:
			m.addFile(item)
		url = m.send()
		return url

	def downloadReport(self, url):
		"""
		Download whole report locally including code diff links
		"""
		mosspy.download_report(url, "submission/report/", connections=8)

	def getLineNumbers(self, diff_link):
		"""
		Get Line Numbers which are same
		"""
		line_nos = []
		list_of_line_nos = []
		page_name = diff_link.split('/')[5].split('.')[0]
		top_frame_name = "-top.html"
		result_link = "http://moss.stanford.edu/results/"
		result_id = diff_link.split('/')[4] + "/"
		result_page = result_link + result_id + page_name + top_frame_name
		
		res = requests.get(result_page, headers={'User-Agent': 'Mozilla/5.0'})
		
		html = bs(res.text, "lxml")
		table = html.find_all('table')[0]
		rows = table.find_all('tr')

		for row in rows:
			columns = row.find_all('td')
			for filename in columns:
				if filename.text.strip() != '':
					line_nos.append(filename.text.strip())
			if line_nos not in list_of_line_nos:
				list_of_line_nos.append(line_nos)
		
		return list_of_line_nos


	def getFormattedDate(self, date_time):
		"""
		Ex : Thu Oct 3 00:16:17 PDT 2019
		timezone is sill PDT, need to change
		"""
		date = date_time[0:18] + date_time[23:len(date_time)]
		date_time_obj = datetime.datetime.strptime(
			str(date), '%c')
		date = str(date_time_obj.date())
		time = str(date_time_obj.time())
		return date, time


	def extractInfo(self, url):
		"""
		Scrape the webpage for percentage match etc.
		"""
		cols = []
		data = []
		
		res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
		html = bs(res.text, "lxml")

		date_time = html.find_all('p')[0]
		date_time = " ".join(date_time.text.split())

		table = html.find_all('table')[0]

		rows = table.find_all('tr')

		for row in rows:
			cols = row.find_all('td')
			for element in cols:
				data.append(element.text.strip())
			
			if len(data) != 0:
				perc = re.findall(r'\d+', data[0]) 
				perc = int(list(map(int, perc))[0])
				result_dict = dict(
					file1 = data[0].split(' ')[0],
					file2 = data[1].split(' ')[0],
					percentage = perc,
					no_of_lines_matched = int(data[2])
				)
				self.results.append(result_dict)

			data.clear()
			# for link in columns:
			# 	if link.a != None:
			# 		result_link = link.a["href"]
			# 		diff_link.append(result_link)

		return self.results


	def getResults(self):
		url = self.submitFiles()
		results = self.extractInfo(url)

		return results, url
