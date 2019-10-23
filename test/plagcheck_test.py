"""Tests for the MOSS interface package for CodeClassroom"""
import unittest
from plagcheck import plagcheck


class TestPlugCheck(unittest.TestCase):
    """Test cases"""

    def test_check(self):
        """General test"""
        program_files = ["testfiles/test_python.py", "testfiles/test_python3.py"]
        language = "python"
        userid = "1"
        url, results = plagcheck.check(program_files, language, userid)
        self.assertIn("http", url)
        self.assertEqual(
            results,
            [
                {
                    "file1": "testfiles/test_python.py",
                    "file2": "testfiles/test_python3.py",
                    "percentage": 90,
                    "no_of_lines_matched": 3,
                    "lines_matched": [["1-3", "1-3"]],
                }
            ],
        )

    def test_perc_str_to_int(self):
        """Test string parsing"""
        result = plagcheck.perc_str_to_int("(42%)")
        self.assertEqual(result, 42)
