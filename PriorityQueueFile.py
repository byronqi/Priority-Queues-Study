import math
from typing import List, TypeVar, Generic, Tuple
import logging

T = TypeVar("T")

logging.basicConfig(level=logging.INFO)  # simple version to the output console
# logging.basicConfig(level=logging.DEBUG, filename=f"log {datetime.datetime.now():%m-%d@%H:%M:%S}.txt",
#                     format="%(asctime)s %(levelname)s %(message)s",
#                     datefmt="%H:%M:%S %p --- ")  # more robust, sent to a file cNode = Tuple[int, T]
Node = Tuple[int, T]


class PriorityQueue(Generic[T]):

    def __init__(self, tree: List[Node] = [], is_min_heap: bool = True):
        self.my_tree: List[Node] = []
        for n in tree:
            self.my_tree.append(n)
        self.is_min_heap = is_min_heap

    def node_at_index(self, index: int) -> Node:
        """
        gives the value stored in node at index
        :param index: location in the tree
        :return: value stored at that location
        postcondition: the tree is unchanged
        raises an indexError if we are out of bounds
        """
        if self.in_bounds(index):
            return self.my_tree[index]
        raise IndexError(f"Index {index} is out of bounds for tree of size {len(self)}")

    def set_node_at_index(self, in_node: Node, index: int):
        """
        changes the node at index to in_node and returns the old node.
        :param in_node: the new node to be stored in this location.
        :param index: location in the tree
        :return: node previously stored at that location
        postcondition: the shape of the tree is unchanged, though content may be changed.
        raises an indexError if we are out of bounds
        """
        if self.in_bounds(index):
            old_node = self.my_tree[index]
            self.my_tree[index] = in_node
            return old_node
        raise IndexError(f"Index {index} is out of bounds for tree of size {len(self)}")

    @staticmethod
    def left_child_of_index(index: int) -> int:
        """
        gives the index of the tree that is directly below and to the left of the given index.
        Note: the index may be out of bounds.
        :param index:
        :return: index of left child of node at index
        """
        return 2 * index + 1

    @staticmethod
    def right_child_of_index(index: int) -> int:
        """
        gives the index of the tree that is directly below and to the right of the given index.
        Note: the index may be out of bounds.
        :param index:
        :return: index of right child of node at index
        """
        return 2 * index + 2

    @staticmethod
    def parent_of_index(index: int) -> int:
        """
        gives the index of the tree that is the parent of the given index
        :param index:
        :return index above the given node index:
        """
        return int((index - 1) / 2)  # yay, integer math!

    def __len__(self):
        return len(self.my_tree)

    def in_bounds(self, index: int) -> bool:
        """
        indicates whether index is within the size of this tree
        :param index:
        :return:
        """
        return 0 <= index < len(self)

    def has_left_child(self, index: int) -> bool:
        """
        indicates whether the node at this index has a child to the left
        :param index:
        :return boolean:
        """
        return self.in_bounds(self.left_child_of_index(index))

    def has_right_child(self, index: int) -> bool:
        """
        indicates whether the node at this index has a child to the right
        :param index:
        :return boolean:
        """
        return self.in_bounds(self.right_child_of_index(index))

    def a_has_priority_over_b(self, a: Node, b: Node) -> bool:
        """
        Determines whether the node "a" has priority over node "b." This is determined by the priorities of "a" and "b"
        and by self.is_min_heap - i.e, should the higher node prevail, or the lower node?
        If the values are equal, then we _do not_ say that the "a" node has priority.
        """
        if self.is_min_heap:
            return a[0] < b[0]
        return a[0] > b[0]

    def is_empty(self) -> bool:
        return len(self) == 0

    def __str__(self):
        """
        Draws a string representation of this tree, without changing it.
        ( you are welcome to examine this code, but you are not responsible for it.)
        :return:
        """
        spaces_per_item = 2 ** (int(
            math.log(len(self)) / math.log(2)) + 2)  # sneaky code to make the tree only as wide as needed.
        result = "-" * (spaces_per_item * 2)
        result += "\n"
        items_per_row = 1
        items_in_current_row = 0
        for item in self.my_tree:
            block = f"{item[0]}:{item[1]}"
            whitespace = " " * int(spaces_per_item - (len(block)) / 2)
            result += f"{whitespace}{block}{whitespace}"
            items_in_current_row += 1
            if items_in_current_row == items_per_row:
                items_in_current_row = 0
                items_per_row *= 2
                spaces_per_item /= 2
                result += "\n"
        return result

    def __repr__(self):
        return self.__str__()

    def to_color_string(self, indices_to_color: List[int] = []):
        """
        Draws a string representation of this tree, without changing it. For all items in the indices list,
        they will show up in a different color.
        This is essentially the same as __str__, but fancy!
        ( you are welcome to examine this code, but you are not responsible for it.)
        :return:
        """
        starters = ["\u001b[31m", "\u001b[32m", "\u001b[33m", "\u001b[34m", "\u001b[35m", "\u001b[36m"]
        reset = "\u001b[0m"

        spaces_per_item = 2 ** (int(
            math.log(len(self)) / math.log(2)) + 2)  # sneaky code to make the tree only as wide as needed.
        result = "-" * (spaces_per_item * 2)
        result += "\n"
        items_per_row = 1
        items_in_current_row = 0
        counter = 0
        for item in self.my_tree:
            block = f"{item[0]}:{item[1]}"
            num_spaces = int(spaces_per_item - (len(block)) / 2)
            if counter in indices_to_color:
                col_num = indices_to_color.index(counter) % len(starters)
                result += starters[col_num]
                result += f"{' ' * num_spaces}{block}{' ' * num_spaces}"
                result += reset
            else:
                result += f"{' ' * num_spaces}{block}{' ' * num_spaces}"

            items_in_current_row += 1
            if items_in_current_row == items_per_row:
                items_in_current_row = 0
                items_per_row *= 2
                spaces_per_item /= 2
                result += "\n"
            counter += 1
        return result

    def to_string_as_list(self):
        """
        creates a string that has one node per line, listed with an index.
        :return:  string with a linear interpretation of the self.tree. Mostly useful for debugging.
        """
        if len(self) == 0:
            return "Empty."
        result = ""
        for i in range(len(self)):
            result += f"{i}:\t{self.my_tree[i]}\n"
        return result

    def clear(self):
        """
        removes all items from this priority queue.
        :return None:
        """
        self.my_tree = []

    def is_a_heap(self) -> bool:
        """
        checks whether the self.my_tree variable holds a representation that is a heap. Any tree is considered a heap
        until you find a child that has greater priority than its parent.
        :return whether _all_ nodes are in a heap-like relationship with parents and children:
        """
        index = 0
        tree_len = self.my_tree.__len__()
        while self.in_bounds(index):
            # ----------------------
            # TODO: You'll be writing this part! Insert your code here.
            for i in range(tree_len):
                if self.has_left_child(i) and self.has_right_child(i):
                    left_has_priority = self.a_has_priority_over_b(self.my_tree[self.left_child_of_index(i)],
                                                  self.my_tree[i])
                    right_has_priority = self.a_has_priority_over_b(
                            self.my_tree[self.right_child_of_index(i)], self.my_tree[i])
                    if left_has_priority or right_has_priority:
                        return False
                if self.has_left_child(i):
                    if self.a_has_priority_over_b(self.my_tree[self.left_child_of_index(i)],
                                                  self.my_tree[i]):
                        return False
            # ----------------------
            index += 1
        logging.info("This is a heap.")
        return True

    def add_value(self, value: T, priority: int = 1):
        """
        adds a node to this data structure and makes sure that the my_tree data structure is
        still a heap.
        :param value: the value to store
        :param priority: its relative weight
        :return None:
        """
        logging.info("-" * 128)
        logging.info(f"Adding: [{priority = }, {value = }]")
        self.my_tree.append((priority, value))  # makes a new, 2-element list and adds it to the main array.
        self.heapify_up(len(self) - 1)
        logging.info(self)

    def heapify_up(self, index: int):
        """
        given the index, potentially swaps itself with its parent, and onward up the tree
        as needed to make this a heap.
        precondition: The node at index is the only one in my_tree that is un-heaplike
        :param index:
        :return None:
        """
        pass
        # ----------------------
        # TODO: You'll be writing this part! Insert your code here.

        while index is not 0:
            current_node: "Node" = self.node_at_index(index)
            parent_node: "Node" = self.node_at_index(self.parent_of_index(index))
            if index is 0:
                break
            else:
                if self.a_has_priority_over_b(current_node, parent_node):
                    self.set_node_at_index(parent_node, index)
                    self.set_node_at_index(current_node, self.parent_of_index(index))
                    index = self.parent_of_index(index)
                else:
                    break
                    # replace original with parent, parent with original

        # tree_len = self.my_tree.__len__()
        # while not self.is_a_heap():
        #     if self.has_left_child(tree_len):
        #         if self.a_has_priority_over_b(self.my_tree[self.left_child_of_index(tree_len)],
        #                                       self.my_tree[self.parent_of_index(tree_len)]):
        #             self.set_node_at_index(self.my_tree[tree_len], self.left_child_of_index(tree_len))
        #     if self.has_right_child(tree_len):
        #         if self.a_has_priority_over_b(self.my_tree[self.right_child_of_index(tree_len)],
        #                                       self.my_tree[self.parent_of_index(tree_len)]):
        #             self.set_node_at_index(self.my_tree[tree_len], self.right_child_of_index(tree_len))
        #     tree_len -= 1
        # ----------------------

    def peek(self) -> Node:
        """
        Gives the node at the start of this Priority Queue without removing it.
        """
        if self.is_empty():
            raise IndexError("Attempted to peek at an empty Queue.")
        return self.my_tree[0]

    def pop(self) -> Node:
        """
        Removes the node at the start of this Priority Queue and resets the Queue so that it is in order; then
        returns the removed node.
        """
        if self.is_empty():
            raise IndexError("Attempted to pop from an empty Queue.")
        result: "Node" = self.my_tree[0]
        self.my_tree[0] = self.my_tree[-1]
        del (self.my_tree[-1])
        logging.info("*" * 128)
        logging.info("Just popped {result}")
        self.heapify_down()
        logging.info(self)
        return result

    def heapify_down(self, index: int = 0):
        """
        The node at index is possibly too high in the tree; we compare it to its children and potentially swap
        it with one of them to put it in better order, and repeat with the node in its new location.
        precondition: the tree is a heap, except possibly for the node at "index."
        postcondition: the tree is once again a heap
        """
        if not self.in_bounds(index):
            return
        print(self.to_color_string([index]))
        current_node: "Node" = self.node_at_index(index)
        left_index: int = self.left_child_of_index(index)
        right_index: int = self.right_child_of_index(index)
        if self.in_bounds(left_index):
            # ----------------------
            # TODO: You'll be writing this part! Insert your code here.
            if self.has_right_child(index):
                right_node = self.node_at_index(right_index)
                left_node = self.node_at_index(left_index)
                if self.a_has_priority_over_b(right_node, current_node):
                    if self.a_has_priority_over_b(right_node, left_node):
                        self.set_node_at_index(right_node, index)
                        self.set_node_at_index(current_node, right_index)
                        # recursive call for right index
                        self.heapify_down(self.right_child_of_index(index))
                        return
                    else:
                        self.set_node_at_index(left_node, index)
                        self.set_node_at_index(current_node, left_index)
                        # recursive call for left index
                        self.heapify_down(self.left_child_of_index(index))
                        return
            if self.has_left_child(index):
                left_node = self.node_at_index(left_index)
                if self.a_has_priority_over_b(left_node, current_node):
                    self.set_node_at_index(left_node, index)
                    self.set_node_at_index(current_node, left_index)
                    # recursive call for left index
                    self.heapify_down(self.left_child_of_index(index))
            # ----------------------
        # Since this tree is complete, we don't need to worry about the right node if the
        # left node was out of bounds.
