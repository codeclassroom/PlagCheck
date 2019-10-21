"""The MOSS interface package for CodeClassroom"""
import re
import requests
import mosspy  # type: ignore
from bs4 import BeautifulSoup as bs  # type: ignore


def download_report(url: str):
    """Download whole report locally including code diff links"""
    mosspy.download_report(url, "submission/report/", connections=8)


def check(program_files: list, lang: str, user_id: str) -> tuple:
    """Check files for same lines"""
    moss = mosspy.Moss(user_id, lang)
    for item in program_files:
        moss.addFile(item)
    url = moss.send()
    results = __extract_info(url)
    return url, results


def __get_line_numbers(url: str) -> list:
    """Get Line Numbers which are same"""

    list_of_line_nos = []
    result_page = re.sub(r".html$", "-top.html", url)

    res = requests.get(result_page, headers={"User-Agent": "Mozilla/5.0"})
    html = bs(res.text, "lxml")
    table = html.find("table")
    # skip header
    for row in table.find_all("tr")[1:]:
        matched_lines = []
        for line_nos in row.find_all("td"):
            line_nos = line_nos.text.strip()
            if line_nos:
                matched_lines.append(line_nos)
        list_of_line_nos.append(matched_lines)
    return list_of_line_nos


def __extract_info(url: str) -> list:
    """Scrape the webpage for file names, percentage match etc."""
    results = []
    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    html = bs(res.text, "lxml")
    table = html.find("table")
    # table looks like this
    # <TABLE>
    # <TR><TH>File 1<TH>File 2<TH>Lines Matched
    # <TR>
    #     <TD><A HREF="http://.../match0.html">testfiles/test_java2.java (92%)</A>
    #     <TD><A HREF="http://.../match0.html">testfiles/test_java3.java (46%)</A>
    #     <TD ALIGN=right>9
    # <TR>
    #     <TD><A HREF="http://.../match1.html">testfiles/test_java.java (87%)</A>
    #     <TD><A HREF="http://.../match1.html">testfiles/test_java3.java (45%)</A>
    #     <TD ALIGN=right>8
    # </TABLE>
    # in order to parse this table we need:
    # skip header
    for row in table.find_all("tr")[1:]:
        # put each column in separate varible
        col1, col2, col3 = row.find_all("td")
        # get matched line ranges from reference from first column
        line_numbers = __get_line_numbers(col1.a.get("href"))
        # get total number of matched lines
        no_of_lines_matched = int(col3.text.strip())
        # get filename and raw percentage stirng from first column
        filename1, perc_str = col1.text.strip().split()
        # get filename from second column
        filename2, ________ = col2.text.strip().split()
        # parse raw percentage from "(45%)" to 45
        match = re.search(r"\((\d+)%\)$", perc_str)
        if match:
            perc = int(match.group(1))
        else:
            raise ValueError("cannot find percentage in table. See " + url)
        result_dict = dict(
            file1=filename1,
            file2=filename2,
            percentage=perc,
            no_of_lines_matched=no_of_lines_matched,
            lines_matched=line_numbers,
        )
        results.append(result_dict)
    return results
