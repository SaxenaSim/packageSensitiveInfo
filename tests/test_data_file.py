import pytest
from src.detection import detection

objDetection = detection()

def test_rdf_empty_name():
    example_string=""
    result = objDetection.read_data_file(example_string)
    assert result == "data/data.txt"
    
def test_rdf_wrong_name():
    example_string="myTest.txt"
    result = objDetection.read_data_file(example_string)
    assert result != "data/data.txt"
    
def test_rdf_cust_name():
    example_string="testData.txt"
    result = objDetection.read_data_file(example_string)
    assert result == "data/testData.txt"
    

