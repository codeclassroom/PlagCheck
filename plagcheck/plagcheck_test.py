"""Tests for the MOSS interface package for CodeClassroom"""
from plagcheck import plagcheck


def test_check():
    """General test"""
    program_files = ["testfiles/test_python.py", "testfiles/test_python3.py"]
    language = "python"
    userid = "1"
    temp = plagcheck.check(language, userid)
    temp.addFile("testfiles/test_python.py")
    temp.addFile("testfiles/test_python3.py")
    temp.submit()
    results = temp.getResults()

    assert results == [
        {
            "file1": "testfiles/test_python.py",
            "file2": "testfiles/test_python3.py",
            "percentage": 90,
            "no_of_lines_matched": 3,
            "lines_matched": [["1-3", "1-3"]],
        }
    ]


def test_perc_str_to_int():
    """Test string parsing"""
    result = plagcheck.perc_str_to_int("(0%)")
    assert result == 0
    result = plagcheck.perc_str_to_int("(42%)")
    assert result == 42
    result = plagcheck.perc_str_to_int("(100%)")
    assert result == 100
