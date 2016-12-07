import unittest


class WordsOrderPositionTest(unittest.TestCase):

    def test_simple_list(self):
        self.assertEqual(toOrderedSet(['foo', 'bar', 'bar', 'xyz']), ['foo', 'bar', 'xyz'])

    def test_empty(self):
        self.assertEqual(toOrderedSet([]), [])

    def test_order_by_nth_simple(self):
        self.assertEqual(toNthOrderedSet(['foo', 'bar', 'xyz', 'bar',], 2), ['foo', 'xyz', 'bar'])

    def test_order_by_nth_empty(self):
        self.assertEqual(toNthOrderedSet([], 2), [])

    def test_order_by_nth_less_than_n(self):
        self.assertEqual(toNthOrderedSet(['foo', 'bar', 'bar', 'xyz', 'foo', 'bar', 'foo', 'bar'], 2), ['bar', 'xyz', 'foo'])

    def test_order_by_nth_None(self):
        self.assertEqual(toNthOrderedSet(None, 5), None)


def toOrderedSet(list):
    if list == None:
        return None

    order = []
    for item in list:
        if not item in order:
            order.append(item)

    return order

def toNthOrderedSet(list, n=1):
    if list is None:
        return None

    tmp_set = {}
    for idx, item in enumerate(list):
        if item in tmp_set:
            if tmp_set[item] < n:
                tmp_set[item] = idx
        else:
            tmp_set[item] = idx

    result = [None] * len(list)

    for item, pos in tmp_set.viewitems():
        result[pos] = item

    return [i for i in result if i != None ]

if __name__ == '__main__':
    unittest.main()
    # pass
