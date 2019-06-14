#!python

from redact_problem import redact_words
import unittest

class RedactTest(unittest.TestCase):
  def test_letters(self):
    list_1 = ['a','a','b','c']
    list_2 = ['c','d','e']
    expected_list = ['a', 'a', 'b']
    assert redact_words(list_1,list_2) == expected_list

  def test_words(self):
    list_3 = ['hello', 'my', 'name']
    list_4 = ['name', 'mi', 'helloo']
    expected_list = ['name']
    assert redact_words(list_3, list_4) == expected_list

  def test_more_words(self):
    list_5 = ['please','shut','up']
    list_6 = ['shut']
    expected_list = ['please', 'up']
    assert redact_words(list_5, list_6) == expected_list

if __name__ == '__main__':
    unittest.main()
