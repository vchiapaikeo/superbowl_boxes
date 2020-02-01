# content of test_unittest_cleandir.py
import unittest

from collections import defaultdict
from server.generate import get_random_names, gen_results


class TestGenerate(unittest.TestCase):

    def test_get_random_names(self):
        num_boxes = 100 
        names_randomized = get_random_names(['Victor', 'Ephraim'], num_boxes)
        self.assertEqual(len(names_randomized), num_boxes)

        # Ensure that there are an equal number of both names
        count_by_name = defaultdict(int)
        for name in names_randomized:
            count_by_name[name] += 1

        values = list(count_by_name.values())
        self.assertEqual(all(x == values[0] for x in values), True)

    def test_gen_results(self):
        num_boxes = 100
        data = gen_results(['Ephraim', 'Victor'], 100)
        self.assertEqual(len(data), 10)
        for arr in data:
            self.assertEqual(len(arr), 10)

