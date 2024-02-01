from lib.check_todo import *

#testing an empty string for todo returns False
def test_check_todo_empty():
    actual = check_todo(" ")
    expected = False
    assert actual == expected 

#testing a string without a todo returns False
def test_check_todo_without():
    actual = check_todo("hello world")
    expected = False
    assert actual == expected 

#testing a string with a #TODO returns True
def test_check_todo_with():
    actual = check_todo("#TODO clean the house")
    expected = True
    assert actual == expected 
