# Description: Min heap implementation with functions add(), get_min()
# remove_min(), and build_heap().
#Implementation note: Does not use any built in python data structures/methods


#Import pre-written DynamicArray and LinkedList classes

from a5_include import *


class MinHeapException(Exception):
    """
    (Skeleton Code) Custom exception to be used by MinHeap class
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        (Skeleton Code) Initializes a new MinHeap
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        (Skeleton Code) Return MH content in human-readable form
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        (Skeleton Code) Return True if no elements in the heap, False otherwise
        """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        """
        adds a new object to the MinHeap maintaining heap property.
        """

        self.heap.append(node)
        node_index = self.heap.length() - 1 #inits node index
        self.perc_up(node_index)

    def get_min(self) -> object:
        """
        returns an object with a minimum key without removing it from the heap. If
        the heap is empty, the method raises a MinHeapException
        """
        if self.is_empty():
            raise MinHeapException
        return self.heap.get_at_index(0)

    def remove_min(self) -> object:
        """
        returns an object with a minimum key and removes it from the heap
        """

        if self.is_empty():
            raise MinHeapException

        retval = self.get_min()

        self.heap.swap(0, self.heap.length()-1)  #Replace first element with last element
        self.heap.pop() #remove last element

        self.perc_down(0)

        return retval

    def build_heap(self, da: DynamicArray) -> None:
        """
        receives a dynamic array with objects in any order and builds a proper
        MinHeap from them
        """

        newheap = DynamicArray()

        for i in range(da.length()): #transfer DA into new variable
            val = da.get_at_index(i)
            newheap.append(val)

        self.heap = newheap

        node_index = (da.length()-1)//2 - 1 #start at PARENT of last node

        while node_index != -1:  #percolates through all non-parent nodes, in reverse
            self.perc_down(node_index)
            node_index -= 1


    def perc_down(self, index):
        """percolates down """
        l_pos = 2*index+1
        r_pos = 2*index+2

        length = self.heap.length()-1
        minimum = index  #current min is the node

        if l_pos <= length and self.heap.get_at_index(index) > self.heap.get_at_index(l_pos):
            minimum = l_pos  #l_pos <= length makes sure l is not beyond the bounds of the array

        if r_pos <= length and self.heap.get_at_index(minimum) > self.heap.get_at_index(r_pos):
            minimum = r_pos

        if minimum != index: # if the node hasn't reached its correct location
            self.heap.swap(index, minimum)
            self.perc_down(minimum)  #call again with minimum as current

    def perc_up(self, index):

        """percolates up """

        p_index = ((index - 1) // 2)  # inits p index, p

        while self.heap.get_at_index(p_index) > self.heap.get_at_index(index) and index != 0:

            self.heap.swap(p_index, index)  # swaps node and parent
            index = p_index  # updates node's index
            p_index = ((index - 1) // 2)  # finds next parent's index

        return

# BASIC TESTING
if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)


    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())


    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty():
        print(h, end=' ')
        print(h.remove_min())


    print("\nPDF - build_heap example 1")
    print("--------------------------")
    #da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    da= DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)
    da.set_at_index(0, 500)
    print(da)
    print(h)
