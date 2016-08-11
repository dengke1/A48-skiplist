import random as r


class Node():
    '''
    A normal node in the skiplist ADT containing a value, a 'down' and an
    'up' reference.
    '''

    def __init__(self, value, next_n, down_n):
        '''
        (Node, object, Node, Node) -> NoneType
        Initializes a node with data, a 'down' and an 'up' reference.
        '''
        self.data = value
        self.next_node = next_n
        self.down_node = down_n


class HeadNode(Node):
    '''
    A head node inheriting from Node. Contains a 'down' and an 'up' reference,
    but no value.
    '''

    def __init__(self, next_n, down_n):
        '''
        (HeadNode, Node, Node) -> NoneType
        Initializes a node with a 'down' and an 'up' reference.
        '''
        Node.__init__(self, None, next_n, down_n)


class TailNode(HeadNode):
    '''
    A Tail node inheriting from Node. Contains a 'down' refence.
    '''

    def __init__(self, down_n):
        '''
        (TailNode, Node) -> NoneType
        Initializes a node with a 'down' reference.
        '''
        HeadNode.__init__(self, None, down_n)


class Skiplist():
    '''
    A class representing a skiplist. Nodes have an up and a down reference, as
    well as a data value. Head nodes contain no data and tail nodes only
    contain down references. There will be only one tail node.
    There will be no extra levels of heads above the other nodes.
    REQ: Data types are comparable
    '''

    def __init__(self, *args):
        '''
        (Skiplist, optional arguments) -> NoneType
        Initializes a skiplist. If no arguments are given the skiplist is
        initialized empty.
        '''
        # keep at 0.5, only have this just in case
        self._f_probability = 0.5
        # initial
        self.tail_node = TailNode(None)
        self.head_node = HeadNode(self.tail_node, None)
        # current node for printing
        self.current_print = self.head_node
        # current node
        self.current = self.head_node
        # node for insertion
        self.added_node = None
        for i in args:
            self.insert(i)

    def the_list(self):
        '''
        (skiplist) -> skiplist
        returns the bottom row of a skiplist, not including the head.
        If empty, return none.
        '''
        current = self.head_node
        # find the bottom headnode
        while current.down_node is not None:
            current = current.down_node
        # check if list is empty
        if isinstance(current.next_node, TailNode):
            return None
        else:
            return current.next_node

    def is_empty(self):
        '''
        (skiplist) -> bool
        returns true or false depending on whether or not the skiplist
        is empty.
        '''
        return self.the_list() is None

    def get_num_node(self, p):
        '''
        (skiplist) -> int
        returns a randomized number using given fixed probability. This will
        represent the number of nodes to be added above the bottom one.
        '''
        num_of_nodes = 0
        # increase num_of_nodes until a number greater or equal to .5 is rolled
        while r.random() < p:
            num_of_nodes += 1
        return num_of_nodes

    def get_height(self):
        '''
        (skiplist) -> int
        returns the height of the list, with bottom row being height of 0.
        '''
        temp = self.head_node
        ret = 0
        # starts at head, counts until bottom is reached
        while temp.down_node is not None:
            ret += 1
            temp = temp.down_node
        return ret

    def add_height(self, num):
        '''
        (Skiplist, int) -> NoneType
        adds a number of head nodes above the list, all pointing to tail
        '''
        # automatically adds one head pointing to current head
        temp = HeadNode(self.tail_node, self.head_node)
        for i in range(num - 1):
            temp = HeadNode(self.tail_node, temp)
        # stack of head is created, self.head_node now points to the top
        self.head_node = temp

    def _add_helper(self, current, value):
        '''
        (Skiplist, Node, obj) -> NoneType
        Adds node inbetween nodes. Only use for when node is to be inserted
        inbetween Nodes and Nodes, Nodes and TailNodes, or HeadNodes
        and TailNodes.
        REQ: current Skiplist height is greater than number of nodes added
        REQ: Skiplist is not empty
        '''
        # base case add node to bottom level of list, down reference is None
        if ((current.down_node is None) and
            (isinstance(current, HeadNode) or (current.data <= value)) and
            ((isinstance(current.next_node, TailNode))
             or (current.next_node.data >= value))):

            temp = current.next_node
            current.next_node = Node(value, temp, None)
            self.added_node = current.next_node

        # base case 2, bottom of list and insert between node and tail
        elif ((current.down_node is None) and not
              (isinstance(current, HeadNode)) and (current.data <= value)
              and (isinstance(current.next_node, TailNode))):

            current.next_node = Node(value, self.tail_node, self.added_node)
            self.added_node = current.next_node

        # else if node is to be added between headnode and tailnode
        # meaning there is another level of nodes to be added
        elif ((isinstance(current, HeadNode)) and
              isinstance(current.next_node, TailNode)):

            self._add_helper(current.down_node, value)
            current.next_node = Node(value, self.tail_node, self.added_node)
            self.added_node = current.next_node

        # else if node is to be inserted between a node and the tail
        elif (not (isinstance(current, HeadNode)) and (current.data <= value)
              and (isinstance(current.next_node, TailNode))):

            self._add_helper(current.down_node, value)
            current.next_node = Node(value, self.tail_node, self.added_node)
            self.added_node = current.next_node

        # else if node is to be inserted between 2 nodes
        elif (not(isinstance(current, HeadNode)) and (current.data < value)
              and (current.next_node.data > value)):

            self._add_helper(current.down_node, value)
            temp = current.next_node
            current.next_node = Node(value, temp, self.added_node)
            self.added_node = current.next_node

        # else if current position is to be moved right
        elif (((not (isinstance(current.next_node, TailNode))) or
               (current.data < value)) and
              (current.next_node.data <= value)):
            self._add_helper(current.next_node, value)

        else:  # if none of above apply, go down to the lower node
            self._add_helper(current.down_node, value)

    def _add_helper_empty_list(self, current, value):
        '''
        (Skiplist, obj, Node, int) -> NoneType
        Populates empty skiplist.
        REQ: skiplist height is the same as the number of nodes to be added
        REQ: skiplist is empty
        '''
        # base case add node to the bottom
        if current.down_node is None:
            current.next_node = Node(value, self.tail_node, None)
            self.added_node = current.next_node

        # else recurse and stack the nodes on top
        else:
            self._add_helper_empty_list(current.down_node, value)
            current.next_node = Node(value, self.tail_node, self.added_node)
            self.added_node = current.next_node

    def check_node_after_head(self, value):
        '''
        (Skiplist, obj) -> bool
        checks if value to be added is less than or equal to the first node
        int the list
        REQ: skiplist is not empty
        '''
        first_node = self.the_list()
        return (first_node.data >= value)

    def _add_helper_after_head(self, current, value):
        '''
        (Skiplist, obj, Node, int) -> NoneType
        Adds nodes right after the head nodes.
        REQ: skiplist height is the same as the number of nodes to be added
        REQ: skiplist is not empty
        '''
        # base case add node to the bottom
        if not isinstance(current.down_node, HeadNode):
            temp = current.next_node
            current.next_node = Node(value, current.next_node, None)
            current.next_node.next_node = temp
            self.added_node = current.next_node

        # else recurse and add the nodes right after the head
        else:
            self._add_helper_after_head(current.down_node, value)
            temp = current.next_node
            current.next_node = Node(value, temp, self.added_node)
            current.next_node.next_node = temp
            self.added_node = current.next_node

    def insert(self, value):
        '''
        (SkipList, obj) -> None
        adds a node with value to the skiplist.
        '''
        # do the random thing and find the number of nodes to be added
        self._num = self.get_num_node(self._f_probability)

        # add heads pointing to tail if current height is less than the
        # number of nodes to be added, if not do nothing
        heads_to_be_added = self._num - self.get_height()
        if heads_to_be_added > 0:
            self.add_height(heads_to_be_added)

        # scroll down to the head node level where nodes are to be added
        self.current = self.head_node
        for i in range(self.get_height() - self._num):
            self.current = self.current.down_node

        # check if list is empty, add nodes if they are
        if self.is_empty():
            self._add_helper_empty_list(self.head_node, value)

        # else check if node to be added needs to be added right after headNode
        elif (self.check_node_after_head(value)):
            self._add_helper_after_head(self.current, value)

        # else check if there are no heads and tails above everything else,
        # if true run _add_helper so that it points to the next node (not head)
        elif (not (isinstance(self.head_node.next_node, TailNode)) and
              (self.head_node.next_node.data < value)):
            self._add_helper(self.current.next_node, value)

        # else use _add_helper and hopefully it works
        # case where there are heads above list
        else:
            self._add_helper(self.current, value)

    def print_helper(self, current):
        '''
        (Skiplist, Node) -> NoneType
        helper to print a representation of a Skiplist.
        '''
        # base case bottom head node
        if isinstance(current, HeadNode) and current.down_node is None:
            while current is not None:
                if isinstance(current, TailNode):
                    self.ret += " -> tail"
                elif isinstance(current, HeadNode):
                    self.ret += "head"
                elif isinstance(current, Node):
                    self.ret += " -> " + str(current.data)
                current = current.next_node
        else:  # recurse
            while current is not None:
                if isinstance(current, TailNode):
                    self.ret += " -> tail" + "\n"
                elif isinstance(current, HeadNode):
                    self.ret += "head"
                elif isinstance(current, Node):
                    self.ret += " -> " + str(current.data)
                current = current.next_node
            self.current_print = self.current_print.down_node
            self.print_helper(self.current_print)

    def __str__(self):
        '''
        (skiplist) -> str
        returns a representation of a Skiplist.
        '''
        self.ret = ""
        self.current_print = self.head_node
        self.print_helper(self.head_node)
        return self.ret

    def _search_helper(self, current, value):
        '''
        (Skiplist, Node, obj) -> Node or None
        Searches for the value in the skiplist. If value is not found,
        None is returned. Otherwise, the node right before the value
        is returned.
        '''
        # case where current is at bottom, and needs to be moved right
        if ((current.down_node is None) and not
            (isinstance(current.next_node, TailNode))
             and (current.next_node.data < value)):
            return self._search_helper(current.next_node, value)

        # base case bottom level of list and item is not found
        elif ((current.down_node is None) and
              ((isinstance(current.next_node, TailNode)) or
               (current.next_node.data != value))):
            return None

        # else if base case 2, item is found
        elif (current.next_node.data == value):
            return current

        # else if current needs to be moved right.
        elif (((isinstance(current, HeadNode)) or (current.data < value))
              and not (isinstance(current.next_node, TailNode)) and
              (current.next_node.data < value)):
            return self._search_helper(current.next_node, value)

        else:  # if none of above apply, go down to the lower node
            return self._search_helper(current.down_node, value)

    def search(self, value):
        '''
        (Skiplist, obj) -> bool
        Returns true if value can be found in skiplist. Otherwise, False is
        returned.
        '''
        if self.is_empty():
            return False
        elif isinstance(self._search_helper(self.head_node, value), Node):
            return True
        else:
            return False

    def remove_helper(self, current, value):
        '''
        (SKiplist, Node, obj) -> NoneType
        removes one row (instance) of value from skiplist.
        REQ: value is in the list
        REQ: current points to the node that points to the value
        '''
        # base case, bottom of list, current's next node is found
        if ((current.down_node is None) and (current.next_node.data == value)):
            current.next_node = current.next_node.next_node

        # elif current's next node is value, remove, recurse down
        elif (current.next_node.data == value):
            self.remove_helper(current.down_node, value)
            current.next_node = current.next_node.next_node

        # elif current's next node is smaller than value, recurse right
        elif (current.next_node.data < value):
            self.remove_helper(current.next_node, value)

    def guillotine(self, current):
        '''
        (Skiplist, Node) -> NoneType
        chops off all heads that point straight to tail
        REQ: current MUST point to head of list
        '''
        # base case if only one level of list
        if ((current.down_node is None) and
            (isinstance(current.next_node,
                        TailNode))):
            self.head_node = current
        elif not isinstance(current.next_node, TailNode):
            self.head_node = current
        else:
            self.guillotine(current.down_node)

    def remove(self, value):
        '''
        (Skiplist, obj) -> NoneType
        removes one row (instance) of the value from skiplist.
        '''
        found_node = self._search_helper(self.head_node, value)
        # removes node only if it's found
        if self.search(value):
            self.remove_helper(found_node, value)
            # remove excess heads
            self.guillotine(self.head_node)
