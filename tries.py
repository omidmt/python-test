class Node(object):
    def __init__(self, c):
        self.char = c
        self.child = {}  # char -> child_Node


class Tries(object):
    EOF_CHAR = '*'
    EOF_NODE = Node(EOF_CHAR)

    def __init__(self):
        self.root = Node('*')
        self.current = self.root

    def add(self, contact, parent=None):
        if len(contact) > 21:
            raise Exception('Illegal argument error: contact length is out of valid range')
        if len(contact) < 1:
            parent.child[Tries.EOF_CHAR] = Tries.EOF_NODE
            return

        if not parent:
            parent = self.root

        if contact[0] in parent.child:
            child = parent.child[contact[0]]
            parent = child
            self.add(contact[1:], parent)
        else:
            node = Node(contact[0])
            parent.child[contact[0]] = node
            self.add(contact[1:], node)

    def count_matched(self, pattern):
        parent = self.root
        for c in pattern:
            if c in parent.child:
                parent = parent.child[c]
            else:
                return 0
        return self.count_childs(parent)

    def count_childs(self, parent):
        # count = len(parent.child)
        count = 0
        for i in parent.child:
            if parent.child[i] == Tries.EOF_NODE:
                count += 1
            else:
                count += self.count_childs(parent.child[i])
        return count


t = Tries()

n = int(raw_input().strip())
for a in xrange(n):
    op, contact = raw_input().strip().split(' ')
    if op == 'add':
        t.add(contact)
    elif op == 'find':
        print t.count_matched(contact)
    else:
        print 'Invalid operation'

