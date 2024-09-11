import unittest
from PriorityQueueFile import PriorityQueue


class MyTestCase(unittest.TestCase):
    def test_heap_1(self):
        # 1/8 Testing a bad heap.
        npq: PriorityQueue[str] = PriorityQueue[str](tree=[[3, "A"], [4, "B"], [5, "C"], [2, "D"]])
        print(npq)  # demo - how to draw what this heap "looks like"
        print(npq.to_string_as_list())
        self.assertFalse(npq.is_a_heap(), "Did not recognize a bad heap.")

    def test_heap_2(self):
        # 2/8 Testing a min heap.
        pq: PriorityQueue[str] = PriorityQueue[str](tree=[[0, "a"], [1, "b"], [2, "c"], [3, "d"], [4, "e"], [5, "f"],
                                                          [6, "g"], [7, "h"], [8, "i"]], is_min_heap=True)
        self.assertTrue(pq.is_a_heap(), "Did not recognize a min heap.")

    def test_heap_3(self):
        # 3/8 Testing a max heap.
        pq2: PriorityQueue[str] = PriorityQueue[str](tree=[[12, "a"], [10, "a"], [8, "a"], [6, "a"], [4, "a"], [2, "a"],
                                                           [0, "a"], [-1, "a"]], is_min_heap=False)
        self.assertTrue(pq2.is_a_heap(), "Did not recognize a max heap.")

    def test_heap_4(self):
        # 4/8 Testing max heap data stored in a min heap.
        pq3: PriorityQueue[str] = PriorityQueue[str](tree=[[12, "a"], [10, "a"], [8, "a"], [6, "a"], [4, "a"], [2, "a"],
                                                           [0, "a"], [-1, "a"]], is_min_heap=True)
        self.assertFalse(pq3.is_a_heap(), "Did not recognize a bad min heap composed of max heap data.")

    def test_heap_5(self):
        # 5/8 Testing a more complicated heap.
        pq4: PriorityQueue[str] = PriorityQueue[str](tree=[[0, "a"], [6, "a"], [3, "a"], [7, "a"], [8, "a"], [4, "a"],
                                                           [10, "a"], [9, "a"], [15, "a"], [11, "a"], [13, "a"],
                                                           [5, "a"]])
        self.assertTrue(pq4.is_a_heap(), "Did not recognize a complicated heap.")

    def test_heap_6(self):
        # q6/8 Test a heap where a child and parent have the same priority.
        pq5: PriorityQueue[str] = PriorityQueue[str](tree=[[0, "a"], [6, "a"], [3, "a"], [6, "a"], [8, "a"], [4, "a"],
                                                           [10, "a"], [9, "a"], [15, "a"], [11, "a"], [13, "a"],
                                                           [5, "a"]])
        self.assertTrue(pq5.is_a_heap(), "A tree with a child and parent with the same value can still be a heap.")

    def test_heap_7(self):
        # 7/8 Testing a singleton heap.
        pq6: PriorityQueue[str] = PriorityQueue[str](tree=[[0, "w"]], is_min_heap=False)
        self.assertTrue(pq6.is_a_heap(), "Did not recognize a singleton heap.")

    def test_heap_8(self):
        # 8/8 Testing an empty heap.
        pq7: PriorityQueue[str] = PriorityQueue[str]()
        self.assertTrue(pq7.is_a_heap(), "Did not recognize an empty heap.")


if __name__ == '__main__':
    unittest.main()
