#!python

from set import Set
import unittest


class SetTest(unittest.TestCase):
    def test_init_and_length(self):
      set_test = Set(['a','b','c'])
      assert set_test.length() == 3
      # adding duplicated
      set_test.add('a')
      assert set_test.length() == 3

    def test_contains(self):
      set_test = Set(['a','b','c'])
      assert set_test.length() == 3
      assert set_test.contains('a') == True
      assert set_test.contains('d') == False
      assert set_test.contains('') == False

    def test_add(self):
      set_test = Set(['a','b','c'])
      assert set_test.length() == 3
      assert set_test.contains('d') == False
      set_test.add('d')
      assert set_test.length() == 4
      assert set_test.contains('d') == True
      assert set_test.contains('e') == False

    def test_remove(self):
      set_test = Set(['a','b','c'])
      assert set_test.length() == 3
      with self.assertRaises(KeyError):
        set_test.remove('d')
      set_test.remove('a')
      assert set_test.length() == 2
      assert set_test.contains('a') == False

    def test_union(self):
      set_test_1 = Set(['a','b','c','c'])
      set_test_2 = Set(['c','d','e','e'])
      assert set_test_1.union(set_test_2).length() == 5

    def test_intersect(self):
      set_test_1 = Set(['a','b','c'])
      set_test_2 = Set(['c','d','e'])
      assert set_test_1.intersection(set_test_2).length() == 1
      set_test_3 = Set(['a','b','c','d'])
      set_test_4 = Set(['e','f','g','h'])
      assert set_test_3.intersection(set_test_4).length() == 0
    
    def test_difference(self):
      set_test_1 = Set(['a','b','c'])
      set_test_2 = Set(['c','d','e'])
      assert set_test_1.difference(set_test_2).length() == 2
      set_test_3 = Set(['a','b','c','d'])
      set_test_4 = Set(['a','b','c','d'])
      assert set_test_3.difference(set_test_4).length() == 0

    def test_subset(self):
      set_test_1 = Set(['a','b','c','c'])
      set_test_2 = Set(['c','a'])
      set_test_3 = Set(['a','d'])
      assert set_test_1.is_subset(set_test_2) is True
      assert set_test_1.is_subset(set_test_3) is False

if __name__ == '__main__':
    unittest.main()
