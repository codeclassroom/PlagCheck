"""Tests for the MOSS interface package for CodeClassroom"""
from plagcheck import plagcheck
from plagcheck import analyze


def test_check():
    """General test"""
    language = "python"
    userid = "1"
    temp = plagcheck.check(language, userid)
    temp.addFilesByWildCard("testfiles/test_python*.py")
    temp.submit()
    results = temp.getResults()
    insights = temp.getInsights()
    share_scores = temp.getShareScores()

    assert share_scores == {
        "testfiles/test_python.py": 2,
        "testfiles/test_python2.py": 2,
        "testfiles/test_python3.py": 2,
    }

    assert insights == {"DCtoC Paths": [], "DtoC Paths": [], "DtoDC Paths": []}

    assert results == [
        {
            "file1": "testfiles/test_python2.py",
            "file2": "testfiles/test_python3.py",
            "lines_matched": [["1-3", "1-3"]],
            "no_of_lines_matched": 3,
            "percentage_file1": 90,
            "percentage_file2": 90,
        },
        {
            "file1": "testfiles/test_python.py",
            "file2": "testfiles/test_python3.py",
            "lines_matched": [["1-3", "1-3"]],
            "no_of_lines_matched": 3,
            "percentage_file1": 90,
            "percentage_file2": 90,
        },
        {
            "file1": "testfiles/test_python.py",
            "file2": "testfiles/test_python2.py",
            "lines_matched": [["1-3", "1-3"]],
            "no_of_lines_matched": 3,
            "percentage_file1": 90,
            "percentage_file2": 90,
        },
    ]


def test_perc_str_to_int():
    """Test string parsing"""
    result = plagcheck.perc_str_to_int("(0%)")
    assert result == 0
    result = plagcheck.perc_str_to_int("(42%)")
    assert result == 42
    result = plagcheck.perc_str_to_int("(100%)")
    assert result == 100


def test_Mgroups():
    """Test Mgroups()"""
    mg = analyze.Mgroups()
    mg.createNodes({"1", "2", "3"})

    mg.relatesTo(45, 88, "3", "1")
    mg.relatesTo(46, 90, "3", "2")

    mg.set_tags()

    assert mg.d2dc() == []
    assert mg.d2c() == [("3", "1"), ("3", "2")]
    assert mg.dc2c() == []
