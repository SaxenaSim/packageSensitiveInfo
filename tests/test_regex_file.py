import pytest, logging
from src.detection import detection

objDetection = detection()

def test_regex_empty_name():
    example_string=""
    result = objDetection.read_regex_file(example_string)
    assert result == "data/patterns.txt"
    
def test_regex_wrong_name():
    example_string="myTest.txt"
    result = objDetection.read_regex_file(example_string)
    assert result != "data/patterns.txt"
    
def test_regex_cust_name():
    example_string="testPatterns.txt"
    result = objDetection.read_regex_file(example_string)
    assert result == "data/testPatterns.txt"
    

