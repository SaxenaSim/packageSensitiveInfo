import pytest
from src.detection import detection

objDetection = detection()

# testing regex when it is present in data
def test_regex_present():
    example_regex= r"\bcredit[_ ]*card[_ ]*number\b"
    example_string="Credit Card number is 12345678"
    result = objDetection.regex_match(example_regex,example_string)
    assert result == True
    
# testing regex when it is not present in data
def test_regex_not_present():
    example_regex= r"\bcredit[_ ]*card[_ ]*number\b"
    example_string="My name is Simran"
    result = objDetection.regex_match(example_regex,example_string)
    assert result == False
    
#Output :  Both test case passed