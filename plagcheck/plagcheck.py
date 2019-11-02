"""The MOSS interface package for CodeClassroom"""

import re
from typing import List, Tuple

import mosspy  # type: ignore
import requests
from bs4 import BeautifulSoup as bs  # type: ignore

HEADERS = {"User-Agent": "Mozilla/5.0"}


class Result(dict):
    """Typing for results"""

    file1: str
    file2: str
    percentage: int
    no_of_lines_matched: int
    lines_matched: List[List[str]]


Results = List[Result]


def download_report(url: str):
    """Download whole report locally including code diff links"""
    mosspy.download_report(url, "submission/report/", connections=8)


def check(program_files: list, lang: str, user_id: str) -> Tuple[str, Results]:
    """Check files for same lines"""
    languages = mosspy.Moss.languages
    if lang not in languages:
        raise ValueError(f"{lang} is not in supported languiges {languages}")
    moss = mosspy.Moss(user_id, lang)
    for item in program_files:
        moss.addFile(item)
    url = moss.send()
    results = __extract_info(url)
    return url, results


def __extract_info(url: str) -> Results:
    """Scrape the webpage for file names, percentage match etc."""
    results: Results = []
    res = requests.get(url, headers=HEADERS)
    html = bs(res.text, "lxml")
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
            lines_matched=__get_line_numbers(col1.a.get("href")),
        )
        results.append(result_dict)
    return results


def __get_line_numbers(url: str) -> List[List[str]]:
    """Get Line Numbers which are same"""

    list_of_line_nos: List[List[str]] = []
    result_page = re.sub(r".html$", "-top.html", url)
    res = requests.get(result_page, headers=HEADERS)
    html = bs(res.text, "lxml")
    table = html.find("table")
    for row in table.find_all("tr")[1:]:
        matched_lines: List[str] = []
        for col in row.find_all("td"):
            line_nos: str = col.text.strip()
            if line_nos:
                matched_lines.append(line_nos)
        list_of_line_nos.append(matched_lines)
    return list_of_line_nos


def perc_str_to_int(string: str) -> int:
    """convert string like "(42%)" to 42"""
    match = re.search(r"\((\d+)%\)$", string)
    if match:
        return int(match.group(1))
    raise ValueError("cannot find percentage in table")
