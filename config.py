"""
This module is used for configuration.
The first two functions return the directory and file extension given.
The third function creates a dictionary.
The remianing functions check for errors
"""
# Error" doesn't conform to snake_case naming style
# pylint: disable=invalid-name

import sys

_UNIGENE_DIR = "/data/PROGRAMMING/assignment5"
_UNIGENE_FILE_ENDING = "unigene"


def get_unigene_directory():
    """
    Returns a directory for file location
    :return: _UNIGENE_DIR"""
    return _UNIGENE_DIR


def get_unigene_extension():
    """
    Returns Extension name
    :return:_UNIGENE_FILE_ENDING
    """
    return _UNIGENE_FILE_ENDING


def get_host_keywords():
    """
    A dictionary of host names, scientific and common
    :return: host_keywords dictionary
    """
    # host names
    homo_sapiens = "Homo_sapiens"
    bos_tarus = "Bos_taurus"
    equus_caballus = "Equus_caballus"
    mus_musculus = "Mus_musculus"
    ovis_aries = "Ovis_aries"
    rattus_norvegicus = "Rattus_norvegicus"

    # make host dict
    host_keywords = {
        "homo sapiens": homo_sapiens,
        "human": homo_sapiens,
        "humans": homo_sapiens,
        "bos taurus": bos_tarus,
        "cow": bos_tarus,
        "cows": bos_tarus,
        "equus caballus": equus_caballus,
        "horse": equus_caballus,
        "horses": equus_caballus,
        "mus musculus": mus_musculus,
        "mouse": mus_musculus,
        "mice": mus_musculus,
        "ovis aries": ovis_aries,
        "sheep": ovis_aries,
        "sheeps": ovis_aries,
        "rattus norvegicus": rattus_norvegicus,
        "rat": rattus_norvegicus,
        "rats": rattus_norvegicus,
    }

    return host_keywords


def get_error_string_4_ValueError():
    """
    Prints error message when invalid argument is entered for ValueError with get_fh()
    """
    print("Invalid argument Value for opening a file for reading/writing", file=sys.stderr)


def get_error_string_4_TypeError():
    """
    Prints error message when invalid argument is entered for TypeError with get_fh()
    """
    print("Invalid argument Type passed in:", file=sys.stderr)


def get_error_string_4_opening_file_OSError(file=None, mode=None):
    """
    Prints error message for OSError
    @param file: file name
    @param mode: mode to open file
    """
    print(f"Could not open the file (os error): {file} with mode {mode}", file=sys.stderr)
