import skiplist as sl


class MultiSet():
    '''
    A multiset is a collection of arbitrary elements where elements can occur
    multiple times. Basically treated like a set. For example, multiset
    {1, 1, 2} is different from multiset {1, 2}
    '''

    def __init__(self, *args):
        '''
        (Multiset) -> None
        initializes a multiset using the skiplist ADT.
        '''
        self.slist = sl.Skiplist()
        for i in args:
            self.insert(i)

    def __contains__(self, element):
        '''
        (MultiSet, anything) -> bool
        returns True if and only if element belongs to the multiset object.
        uses in
        '''
        return self.slist.search(element)

    def count(self, element):
        '''
        (MultiSet, anything) -> int
        Returns the number of occurrences of element e in multiset s.
        '''
        temp = self.slist.the_list()
        count = 0
        # check if self is empty
        if len(self) == 0:
            return count
        while temp.data is not None:
            if element == temp.data:
                count += 1
            temp = temp.next_node
        return count

    def insert(self, element):
        '''
        (MultiSet, anything) -> NoneType
        inserts element into multiset.
        '''
        self.slist.insert(element)

    def remove(self, element):
        '''
        (MultiSet, anything) -> NoneType
        Removes one occurence of an element from the MultiSet.
        If the element is not present, do nothing.
        '''
        self.slist.remove(element)

    def clear(self):
        '''
        (MultiSet) -> NoneType
        Removes all elements from the MultiSet.
        '''
        self.slist = sl.Skiplist()

    def __len__(self):
        '''
        (MultiSet) -> int
        Returns the number of elements in the MultiSet.
        uses len()
        '''
        if self.slist.is_empty():
            return 0
        else:
            temp = self.slist.the_list()
            count = 0
            while temp.data is not None:
                count += 1
                temp = temp.next_node
            return count

    def __repr__(self):
        '''
        (MultiSet) -> str
        returns a string representation of the MultiSet, where each element
        printed is one occurrence of one element in the MultiSet.
        uses repr()
        '''
        # get the bottom of the list
        temp = self.slist.the_list()
        # if skiplist isn't empty
        if not self.slist.is_empty():
            ret = "MultiSet([" + str(temp.data)
            temp = temp.next_node
            # go throught every node and add the data
            while temp.data is not None:
                ret += ", " + str(temp.data)
                temp = temp.next_node
            ret += "])"
        else:
            ret = "MultiSet([])"
        return ret

    def __eq__(self, set2):
        '''
        (MultiSet) -> bool
        Returns True if and only if MultiSet 1 contains exactly the same
        elements as MultiSet 2. The number of occurrences of each element
        need to be the same too.
        Uses ==
        REQ: set2 is a Multiset
        '''
        temp1 = self.slist.the_list()
        temp2 = set2.slist.the_list()
        # if both empty then return true
        if self.slist.is_empty() and set2.slist.is_empty():
            is_equal = True
        # elif only one is empty return false
        elif ((self.slist.is_empty() and not set2.slist.is_empty()) or
              (set2.slist.is_empty() and not set1.slist.is_empty())):
            is_equal = False
        else:
            is_equal = True
            while temp1 is not None and temp2 is not None and is_equal:
                if temp1.data == temp2.data:
                    is_equal = True
                else:
                    is_equal = False
                temp1 = temp1.next_node
                temp2 = temp2.next_node
        return is_equal

    def __le__(self, set2):  # error, try (2, 2, 2) and (1, 2, 3)
        '''
        (MultiSet, MultiSet) -> bool
        Returns True if and only if MultiSet 1 is a subset of MultiSet 2 or
        is equal to MultiSet 2.
        Uses <=
        '''
        temp1 = self.slist.the_list()
        temp2 = set2.slist.the_list()
        if len(self) > len(set2):
            return False
        else:
            return self.__sub__(set2).slist.is_empty()

    def __sub__(self, set2):
        '''
        (MultiSet, Multiset) -> MultiSet
        returns a new MultiSet that contains every element that belongs to
        MultiSet 1 but not to MultiSet 2. The returned MultiSet is the
        difference of MultiSets 1 and 2.
        Uses -
        '''
        temp1 = self
        bot2 = set2.slist.the_list()
        # check if set2 is empty
        if len(set2) == 0:
            return temp1
        while bot2.data is not None:
            temp1.remove(bot2.data)
            bot2 = bot2.next_node
        return temp1

    def __isub__(self, set2):
        '''
        (MultiSet, MultiSet) -> NoneType
        Updates MultiSet 1 so that every element present in MultiSet 2 is
        removed from MultiSet 1.
        Uses -=
        '''
        bot2 = set2.slist.the_list()
        # check if set2 is empty
        if len(set2) == 0:
            return self
        while bot2.data is not None:
            self.remove(bot2.data)
            bot2 = bot2.next_node
        return self

    def __add__(self, set2):
        '''
        (MultiSet, MultiSet) -> MultiSet
        Returns a new MultiSet that is the union of MultiSets 1 and 2.
        Uses +
        '''
        temp1 = self
        bot2 = set2.slist.the_list()
        # check if set2 is empty
        if len(set2) == 0:
            return temp1
        while bot2.data is not None:
            temp1.insert(bot2.data)
            bot2 = bot2.next_node
        return temp1

    def __iadd__(self, set2):
        '''
        (MultiSet, MultiSet) -> NoneType
        Updates MultiSet 1 so that every element in MultiSet 2 is added to
        MultiSet 1.
        Uses +=
        '''
        bot2 = set2.slist.the_list()
        # check if set2 is empty
        if len(set2) == 0:
            return temp1
        while bot2.data is not None:
            self.insert(bot2.data)
            bot2 = bot2.next_node
        return self

    def __and__(self, set2):
        '''
        (MultiSet, MultiSet) -> MultiSet
        Returns a new MultiSet that contains every element that belongs to
        both MultiSet 1 and 2. New MultiSet is the intersection of the
        previous two.
        Uses &
        '''
        # initialize stuff
        temp1 = self.slist.the_list()
        temp2 = set2.slist.the_list()
        self._temp_set = MultiSet()
        # check if both lists are empty
        if len(set2) == 0 or len(self) == 0:
            return self._temp_set
        # go through lists
        while (temp1.data is not None) and (temp2.data is not None):
            # if nodes' datas are equal add them into new list
            # move to next nodes
            if temp1.data == temp2.data:
                self._temp_set.insert(temp1.data)
                temp1 = temp1.next_node
                temp2 = temp2.next_node
            # If temp1's data is smaller, move on to temp1's next node
            elif temp1.data < temp2.data:
                temp1 = temp1.next_node
            # else temp1's data is bigger, move to temp2's next node
            else:
                temp2 = temp2.next_node
        return self._temp_set

    def __iand__(self, set2):
        '''
        (MultiSet, MultiSet) -> NoneType
        Changes MultiSet 1 so that it only contains elements present to both
        MultiSet 1 and 2.
        Uses &=
        '''
        temp1 = self.slist.the_list()
        temp2 = set2.slist.the_list()
        # check if both lists are empty
        if len(set2) == 0 or len(self) == 0:
            return self
        self.clear()
        # go through lists
        while (temp1.data is not None) and (temp2.data is not None):
            # if nodes' datas are equal add them into new list
            # move to next nodes
            if temp1.data == temp2.data:
                self.insert(temp1.data)
                temp1 = temp1.next_node
                temp2 = temp2.next_node
            # If temp1's data is smaller, move on to temp1's next node
            elif temp1.data < temp2.data:
                temp1 = temp1.next_node
            # else temp1's data is bigger, move to temp2's next node
            else:
                temp2 = temp2.next_node
        return self

    def isdisjoint(self, set2):
        '''
        (MultiSet, MultiSet) -> bool
        Returns True if and only if MultiSet 1 has no element in common with
        MultiSet 2.
        '''
        return self.__and__(set2).slist.is_empty()
