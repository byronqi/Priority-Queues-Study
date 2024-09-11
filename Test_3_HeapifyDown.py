import unittest
from PriorityQueueFile import PriorityQueue


class MyTestCase(unittest.TestCase):
    def test_heapify_Down_1(self):
        """
        checks whether a single-step heapify down works.
        :return:
        """
        items = [(0, 1), (1, 2), (4, 5), (6, 11), (7, 13), (8, 17), (5, 7), (9, 19), (2, 3)]
        expected = [(0, 1), (1, 2), (4, 5), (2, 3), (7, 13), (8, 17), (5, 7), (9, 19), (6, 11)]

        pq: PriorityQueue[int] = PriorityQueue[int](tree=items, is_min_heap=True)

        self.assertFalse(pq.is_a_heap(), "This tree should not start as a heap!")
        pq.heapify_down(index=3)
        self.assertEqual(expected, pq.my_tree, "Result did not match expected value.")

    def test_heapify_Down_2(self):
        """
        tests whether a choice between two equal priority children is handled correctly.
        :return:
        """
        items = [(2, 'Happy'), (11, 'Dopey'), (5, 'Sneezy'), (7, 'Grumpy'), (7, 'Sleepy'), (8, 'Doc'), (6, 'Bashful')]
        distractor = [(2, 'Happy'), (7, 'Sleepy'), (5, 'Sneezy'), (7, 'Grumpy'), (11, 'Dopey'), (8, 'Doc'),
                      [6, 'Bashful']]
        expected = [(2, 'Happy'), (7, 'Grumpy'), (5, 'Sneezy'), (11, 'Dopey'), (7, 'Sleepy'), (8, 'Doc'),
                    (6, 'Bashful')]

        pq: PriorityQueue[str] = PriorityQueue[str](tree=items, is_min_heap=True)

        self.assertFalse(pq.is_a_heap(), "This should not start off as a heap.")
        pq.heapify_down(index=1)
        self.assertTrue(pq.is_a_heap(), "The heapify down should have turned this into a heap.")
        self.assertNotEqual(distractor, pq.my_tree,
                            "Although the queue is a heap, when confronted with the need to swap with one of two "
                            "equal children, the choice should be to swap left.")

        self.assertEqual(expected, pq.my_tree,
                         "When confronted with the need to swap with one of two equal children, the choice should "
                         "be to swap left.")

    def test_heapify_Down_3(self):
        """
        tests whether a single child and parent of equal priority will be swapped.
        :return:
        """
        items = [(1, "A"), (1, "B"), (1, "C"), (1, "D"), (0, "E"), (1, "F"), (1, "G"), (0, "H"), (0, "I"), (0, "J"),
                 (0, "K")]

        pq: PriorityQueue[str] = PriorityQueue[str](tree=items, is_min_heap=False)

        pq.heapify_down(4)
        self.assertEqual(items, pq.my_tree,
                         "heapifying down between a parent and one child with same priority should not change "
                         "anything.")

    def test_heapify_Down_4(self):
        """
        tests whether 2 children and parent of equal priority will be swapped.
        :return:
        """
        items = [(1, "A"), (1, "B"), (1, "C"), (1, "D"), (1, "E"), (1, "F"), (1, "G"), (1, "H"), (1, "I"), (1, "J"),
                 (1, "K")]

        pq: PriorityQueue[str] = PriorityQueue[str](tree=items, is_min_heap=False)

        pq.heapify_down(4)
        self.assertEqual(items, pq.my_tree,
                         "heapifying down between a parent and two children all with same priority "
                         "should not change anything.")

    def test_heapify_Down_5(self):
        """
        checks whether a heapify down from the root for a multistage tree works.
        :return:
        """
        items = [(26, 'TX'), (47, 'NM'), (50, 'HI'), (38, 'CO'), (46, 'OK'), (49, 'AK'), (30, 'WI'), (33, 'OR'),
                 (37, 'NB'), (41, 'MT'), (45, 'UT'), (48, 'AZ'), (24, 'MI'), (26, 'MI'), (29, 'IA'), (17, 'OH'),
                 (32, 'MN'), (34, 'KS'), (36, 'NV'), (21, 'IL'), (40, 'SD'), (42, 'WA'), (44, 'WY'), (25, 'AR'),
                 (31, 'CA'), (6, 'MA'), (23, 'ME'), (5, 'CT'), (13, 'RI'), (12, 'NC'), (27, 'FL'), (1, 'DE'),
                 (10, 'VA'), (7, 'MD'), (22, 'AL'), (4, 'GA'), (16, 'TN'), (15, 'KY'), (35, 'WV'), (3, 'NJ'),
                 (18, 'LA'), (9, 'NH'), (39, 'ND'), (8, 'SC'), (20, 'MS'), (19, 'IN'), (43, 'ID'), (2, 'PA'),
                 (14, 'VT'), (11, 'NY')]

        expected = [(50, 'HI'), (47, 'NM'), (49, 'AK'), (38, 'CO'), (46, 'OK'), (48, 'AZ'), (30, 'WI'), (33, 'OR'),
                    (37, 'NB'), (41, 'MT'), (45, 'UT'), (31, 'CA'), (24, 'MI'), (26, 'MI'), (29, 'IA'), (17, 'OH'),
                    (32, 'MN'), (34, 'KS'), (36, 'NV'), (21, 'IL'), (40, 'SD'), (42, 'WA'), (44, 'WY'), (25, 'AR'),
                    (26, 'TX'), (6, 'MA'), (23, 'ME'), (5, 'CT'), (13, 'RI'), (12, 'NC'), (27, 'FL'), (1, 'DE'),
                    (10, 'VA'), (7, 'MD'), (22, 'AL'), (4, 'GA'), (16, 'TN'), (15, 'KY'), (35, 'WV'), (3, 'NJ'),
                    (18, 'LA'), (9, 'NH'), (39, 'ND'), (8, 'SC'), (20, 'MS'), (19, 'IN'), (43, 'ID'), (2, 'PA'),
                    (14, 'VT'), (11, 'NY')]

        pq: PriorityQueue[str] = PriorityQueue[str](tree=items, is_min_heap=False)

        # print(pq.to_color_string())
        self.assertFalse(pq.is_a_heap(), "The queue should not initially show up as a heap!")
        pq.heapify_down(index=0)
        self.assertTrue(pq.is_a_heap(), "The queue should become a heap.")
        self.assertEqual(pq.my_tree, expected, "The tree did not wind up with the correct order.")

    def test_heapify_Down_6(self):
        pq: PriorityQueue[str] = PriorityQueue[str](is_min_heap=True)
        items = [(0, "AB"), (7, "CD"), (3, "EF"), (4, "GH"), (8, "IJ"), (10, "KL"), (5, "MN"), (13, "OP"), (6, "QR"),
                 (12, "ST"), (2, "UV"), (1, "WX"), (9, "YZ")]
        items_after_pop = [(1, 'WX'), (2, 'UV'), (3, 'EF'), (6, 'QR'), (4, 'GH'), (9, 'YZ'), (5, 'MN'), (13, 'OP'),
                           (7, 'CD'), (12, 'ST'), (8, 'IJ'), (10, 'KL')]
        items_after_pop2 = [(2, 'UV'), (4, 'GH'), (3, 'EF'), (6, 'QR'), (8, 'IJ'), (9, 'YZ'), (5, 'MN'), (13, 'OP'),
                            (7, 'CD'), (12, 'ST'), (10, 'KL')]
        expected_sorted = [(2, 'UV'), (3, 'EF'), (4, 'GH'), (5, 'MN'), (6, 'QR'), (7, 'CD'), (8, 'IJ'), (9, 'YZ'),
                           (10, 'KL'), (12, 'ST'), (13, 'OP')]

        for item in items:
            pq.add_value(value=item[1], priority=item[0])

        sorted_items = []
        self.assertEqual((0, "AB"), pq.pop(), "Failed to pop smallest priority item from minHeap.")
        self.assertEqual(items_after_pop, pq.my_tree, "myTree is no longer a min heap.")
        self.assertEqual((1, "WX"), pq.pop(), "Failed to pop second smallest priority item from minHeap.")
        self.assertEqual(items_after_pop2, pq.my_tree, "myTree is no longer a min heap after second pop.")
        while not pq.is_empty():
            sorted_items.append(pq.pop())

        self.assertEqual(expected_sorted, sorted_items,
                         f"Items were not removed in correct order.\n{expected_sorted = }\n"
                         f"{         sorted_items = }")

    def test_heapify_Down_7(self):
        """
        tests whether heapify down works correctly with a heap of an even number of items, and we are heapifying down to
        the right....
        :return:
        """
        items = [(6, 'Jrnl'), (2, 'Dance'), (1, 'Choir'), (9, 'Theat'), (5, 'Photo'), (7, 'Film'), (3, 'Ceram'),
                 (13, 'Orch'), (11, 'ChTh'), (14, 'MxMd'), (8, 'DrwPt'), (10, 'Tech'), (12, 'Sclp'), (4, 'Band')]

        expected = [(1, 'Choir'), (2, 'Dance'), (3, 'Ceram'), (9, 'Theat'), (5, 'Photo'), (7, 'Film'), (4, 'Band'),
                    (13, 'Orch'), (11, 'ChTh'), (14, 'MxMd'), (8, 'DrwPt'), (10, 'Tech'), (12, 'Sclp'), (6, 'Jrnl')]

        pq: PriorityQueue[str] = PriorityQueue[str](tree=items, is_min_heap=True)

        pq.heapify_down(index=0)
        self.assertEqual(expected, pq.my_tree,
                         "Heapify_down for a heap with an even number of nodes where we heapify mostly "
                         "to the right")


if __name__ == '__main__':
    unittest.main()
