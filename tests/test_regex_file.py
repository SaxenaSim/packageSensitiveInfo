import pytest, logging
from src.detection import detection

objDetection = detection()

# testing patterns file with default value
def test_regex_empty_name():
    example_string=""
    result = objDetection.read_regex_file(example_string)
    assert result == "data/patterns.txt"
 
 # testing patterns file with wrong file name   
def test_regex_wrong_name():
    example_string="myTest.txt"
    result = objDetection.read_regex_file(example_string)
    assert result != "data/patterns.txt"
 
 # testing patterns file with user file name   
def test_regex_cust_name():
    example_string="testPatterns.txt"
    result = objDetection.read_regex_file(example_string)
    assert result == "data/testPatterns.txt"
    

# Output : All test case passed