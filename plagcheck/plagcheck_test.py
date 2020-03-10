"""Tests for the MOSS interface package for CodeClassroom"""
from plagcheck import analyze, plagcheck
from plagcheck.plagcheck import insights, share_scores


def test_check():
    """General test"""
    language = "python"
    userid = "1"
    temp = plagcheck.check(language, userid)
    temp.addFile("testfiles/test_python.py")
    temp.addFile("testfiles/test_python2.py")
    temp.submit()
    results = temp.getResults()
    moss_insights = insights(results)
    moss_share_scores = share_scores(results)

    assert moss_share_scores == {
        "testfiles/test_python.py": 1,
        "testfiles/test_python2.py": 1,
    }

    assert moss_insights == {"DCtoC Paths": [], "DtoC Paths": [], "DtoDC Paths": []}

    assert results == [
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

    mg.relate(45, 88, "3", "1")
    mg.relate(46, 90, "3", "2")

    mg.set_tags()

    assert mg.d2dc() == []
    assert mg.d2c() == [("3", "1"), ("3", "2")]
    assert mg.dc2c() == []
