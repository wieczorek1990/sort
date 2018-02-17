import unittest

import sort


class SortTest(unittest.TestCase):
    def setUp(self):
        self.before = [5, 4, 4, 3, 1, 2]
        self.after = [1, 2, 3, 4, 4, 5]

    def swap(self):
        self.assertEqual(sort.swap(self.before, 0, 1), [4, 5, 4, 3, 1, 2])

    def test_bubble_sort(self):
        self.assertEqual(sort.bubble_sort(self.before), self.after)

    def test_minimum(self):
        self.assertEqual((4, 1), sort.minimum(self.before, 0))

    def test_selection_sort(self):
        self.assertEqual(sort.selection_sort(self.before), self.after)

    def test_select_pivot(self):
        self.assertEqual(sort.select_pivot(0, 2), 1)

    def test_select_pivot(self):
        self.assertEqual(sort.divide_array(self.before, 0, 1), 1)

    def test_qsort(self):
        self.assertEqual(sort.qsort(self.before), self.after)


if __name__ == '__main__':
    unittest.main()
