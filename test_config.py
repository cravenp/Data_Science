"""
Test suite for config.py
"""
# ignore all "Missing function or method docstring" since this is a unit test
# pylint: disable=C0116
# ignore unconventional function naming
# pylint: disable=C0103


from assignment5 import config


UNIGENE_DIR = "/data/PROGRAMMING/assignment5"
_UNIGENE_FILE_ENDING = "unigene"


def test_get_unigene_directory():
    """Test return of directory name"""
    test_dir = config.get_unigene_directory()
    assert test_dir == UNIGENE_DIR


def test_get_unigene_extension():
    """Test return of extension name"""
    test_ext = config.get_unigene_extension()
    assert test_ext == _UNIGENE_FILE_ENDING


def test_get_host_keywords():
    """Test dictionary retrival"""
    test_value = config.get_host_keywords()
    test_result = test_value["human"]
    assert test_result == "Homo_sapiens"
