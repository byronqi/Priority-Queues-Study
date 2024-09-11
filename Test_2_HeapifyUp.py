import unittest
from PriorityQueueFile import PriorityQueue


class MyTestCase(unittest.TestCase):

    def test_heap_add_1(self):
        # creating a min heap
        pq = PriorityQueue(is_min_heap=True)
        items = [[0, "AB"], [7, "CD"], [3, "EF"], [4, "GH"], [8, "IJ"], [10, "KL"], [5, "MN"], [13, "OP"], [6, "QR"],
                 [12, "ST"], [2, "UV"], [1, "WX"], [9, "YZ"]]

        min_heap_tree = [(0, 'AB'), (2, 'UV'), (1, 'WX'), (6, 'QR'), (4, 'GH'), (3, 'EF'), (5, 'MN'), (13, 'OP'),
                         (7, 'CD'), (12, 'ST'), (8, 'IJ'), (10, 'KL'), (9, 'YZ')]

        for item in items:
            pq.add_value(value=item[1], priority=item[0])

        self.assertEqual(pq.my_tree, min_heap_tree, "Did not create a min heap.")

    def test_heap_add_2(self):
        # creating a max heap
        pq = PriorityQueue(is_min_heap=False)
        items = [[0, "AB"], [7, "CD"], [3, "EF"], [4, "GH"], [8, "IJ"], [10, "KL"], [5, "MN"], [13, "OP"], [6, "QR"],
                 [12, "ST"],
                 [2, "UV"], [1, "WX"], [9, "YZ"]]

        max_heap_tree = [(13, 'OP'), (12, 'ST'), (9, 'YZ'), (7, 'CD'), (10, 'KL'), (8, 'IJ'), (5, 'MN'), (0, 'AB'),
                         (6, 'QR'), (4, 'GH'), (2, 'UV'), (1, 'WX'), (3, 'EF')]

        for item in items:
            pq.add_value(value=item[1], priority=item[0])

        self.assertEqual(pq.my_tree, max_heap_tree, "Did not create a max heap.")

    def test_heap_add_3(self):
        # creating a min heap with duplicate priorities
        pq = PriorityQueue(is_min_heap=True)
        items = [[3, "ZY"], [2, "XW"], [4, "VU"], [1, "TS"], [2, "RQ"]]

        distractor = [(1, 'TS'), (2, 'RQ'), (4, 'VU'), (3, 'ZY'), (2, 'XW')]
        expected = [(1, 'TS'), (2, 'XW'), (4, 'VU'), (3, 'ZY'), (2, 'RQ')]

        for item in items:
            pq.add_value(value=item[1], priority=item[0])

        self.assertTrue(pq.is_a_heap(), "The tree should have become a heap.")
        self.assertNotEqual(distractor, pq.my_tree, "Tree with two equal priorities did create heap, but tie "
                                                    "should not have pushed original down.")
        self.assertEqual(expected, pq.my_tree, "Tree results are incorrect.")


if __name__ == '__main__':
    unittest.main()
