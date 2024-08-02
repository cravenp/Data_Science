"""
Test suite for my_io.py
"""
# ignore all "Missing function or method docstring" since this is a unit test
# pylint: disable=C0116
# ignore unconventional function naming
# pylint: disable=C0103

import os
import pytest
from assignment4.my_io import get_fh


FH_TEST_OUT = "file.txt"


def test_get_fh_4_read():
    """Test read functionality"""
    fh_h = get_fh(FH_TEST_OUT, 'w')
    fh_h.write("test")
    fh_h.close()
    fh_read = get_fh(FH_TEST_OUT, 'r')
    assert "test" in fh_read.read()
    assert hasattr(fh_h, "readline") is True, "Not able to open for reading"
    fh_read.close()
    os.remove(FH_TEST_OUT)


def test_get_fh_4_write():
    """Test write functionality"""
    fh_h = get_fh(FH_TEST_OUT, 'w')
    fh_h.write("test")
    assert hasattr(fh_h, "write") is True, "Not able to open for writing"
    fh_h.close()
    os.remove(FH_TEST_OUT)


def test_get_fh_4_OSError():
    """Test OS Error"""
    with pytest.raises(OSError):
        get_fh("doesntwork.txt", "r")


def test_get_fh_4_ValueError():
    """Test ValueError"""
    with pytest.raises(ValueError):
        get_fh("ss.txt", "rrr")
