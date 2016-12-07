def find(x, sarr, xcl_idx=None):
    """ sarr sorted array of tuple (idx, cost) to search in
        x searching term
        return index of matched element
    """
    left = 0
    right = len(sarr) - 1

    if x > sarr[right][1] or x < sarr[left][1]:
        return None
    while left <= right:
        # print left
        # print right
        mid = (right - left) / 2 + left
        if x == sarr[mid][1] and xcl_idx != sarr[mid][0]:
            return sarr[mid]
        if x < sarr[mid][1]:
            right = mid - 1
        else:
            left = mid + 1
    return None


def match_price(m, a):
    if len(a) < 2:
        raise Exception('Wrong price list')
    price_list = map(lambda x: x, enumerate(a))
    price_list = sorted(price_list, key=lambda price: price[1])
    for p in price_list:
        remainder = m - p[1]
        j = find(remainder, price_list, p[0])
        if j:
            return (p[0] + 1, j[0] + 1) if j[0] > p[0] else (j[0] + 1, p[0] + 1)


t = int(raw_input().strip())
for a0 in xrange(t):
    m = int(raw_input().strip())
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split(' '))
    result = match_price(m, a)
    # print result
    print str(result[0]) + ' ' + str(result[1])


# Sample input
# 1
# 8
# 8
# 2 1 9 4 4 56 90 3

# Sample output
# 4 5
