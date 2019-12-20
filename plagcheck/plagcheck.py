"""The MOSS interface package for CodeClassroom"""
import re
from typing import List, Tuple

import mosspy
import urllib.request
from bs4 import BeautifulSoup as bs

HEADERS = {"User-Agent": "Mozilla/5.0"}


class Result(dict):
    """Typing for moss results"""

    file1: str
    file2: str
    percentage: int
    no_of_lines_matched: int
    lines_matched: List[List[str]]


Results = List[Result]


def perc_str_to_int(string: str) -> int:
    """
    Convert string like "(42%)" to 42
    """
    match = re.search(r"\((\d+)%\)$", string)
    if match:
        return int(match.group(1))
    raise ValueError("Cannot find percentage in table")


class check:
    def __init__(self, files: list, lang: str, user_id: str):

        self.__user_id = user_id
        self.files = files
        languages = mosspy.Moss.languages
        if lang not in languages:
            raise ValueError(f"{lang} is not a supported language {languages}")
        self.lang = lang
        self.__moss = mosspy.Moss(self.__user_id, self.lang)

    def __extract_info(self) -> Results:
        """
        Scrape the webpage for file names, percentage match etc.
        """
        results: Results = []

        req = urllib.request.Request(self.home_url, headers=HEADERS)
        with urllib.request.urlopen(req) as response:
            req = response.read()

        html = bs(req.decode("utf-8"), "lxml")
        table = html.find("table")
        for row in table.find_all("tr")[1:]:
            col1, col2, col3 = row.find_all("td")
            filename1, perc = col1.text.strip().split()
            filename2, ____ = col2.text.strip().split()
            result_dict = Result(
                file1=filename1,
                file2=filename2,
                percentage=perc_str_to_int(perc),
                no_of_lines_matched=int(col3.text.strip()),
                lines_matched=self.__get_line_numbers(col1.a.get("href")),
            )
            results.append(result_dict)
        return results

    def __get_line_numbers(self, url: str) -> List[List[str]]:
        """
        Get Line Numbers which are same
        """
        list_of_line_nos: List[List[str]] = []
        result_page = re.sub(r".html$", "-top.html", url)

        req = urllib.request.Request(result_page, headers=HEADERS)
        with urllib.request.urlopen(req) as response:
            req = response.read()

        html = bs(req.decode("utf-8"), "lxml")
        table = html.find("table")
        for row in table.find_all("tr")[1:]:
            matched_lines: List[str] = []
            for col in row.find_all("td"):
                line_nos: str = col.text.strip()
                if line_nos:
                    matched_lines.append(line_nos)
            list_of_line_nos.append(matched_lines)
        return list_of_line_nos

    def addBase(self, base_file: str):
        """
        Add basefile
        """
        self.__moss.addBaseFile(base_file)

    def submit(self):
        """
        Submit files to the Moss Server
        """
        for item in self.files:
            self.__moss.addFile(item)
        url = self.__moss.send()

        self.home_url = url

    def getHomePage(self):
        """
        Return Moss Results HomePage URL
        """
        return self.home_url

    def getResults(self) -> Tuple[str, Results]:
        """
        Return the result as a list of dictionary
        """
        results = self.__extract_info()

        return results
