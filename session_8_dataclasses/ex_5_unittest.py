"""
Suppose you have a function called find_duplicate_numbers that takes in a list of numbers
and returns a list of any duplicate numbers in that list. Write some unittests to test
the correctness of this function.

Here's an example implementation of the find_duplicate_numbers function:

[1, 2, 3, 4], []
[1, 2, 2, 3, 4]), [2]

"""

import unittest


def find_duplicate_numbers(numbers):
    seen = set()
    duplicates = set()
    for number in numbers:
        if number in seen:
            duplicates.add(number)
        else:
            seen.add(number)
    return list(duplicates)


class TestFindDuplicateNumbers(unittest.TestCase):
    def test_no_duplicates(self):
        self.assertEqual(find_duplicate_numbers([1, 2, 3, 4]), [])

    def test_one_duplicate(self):
        self.assertEqual(find_duplicate_numbers([1, 2, 2, 3, 4]), [2])

    def test_multiple_duplicates(self):
        self.assertEqual(find_duplicate_numbers([1, 2, 2, 3, 3, 3, 4]), [2, 3])

    def test_empty_list(self):
        self.assertEqual(find_duplicate_numbers([]), [])

    def test_all_duplicates(self):
        self.assertEqual(find_duplicate_numbers([1, 1, 1, 1]), [1])

if __name__ == '__main__':
    unittest.main()