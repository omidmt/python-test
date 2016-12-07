"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    search_array = input_array
    count = 0
    while len(search_array)/2 > 0:
        count += 1
        if(search_array[len(search_array)/2] > value):
            search_array = search_array[:len(search_array)/2]
        elif(search_array[len(search_array)/2] < value):
            search_array = search_array[len(search_array)/2:]
        else:
            return count + len(search_array)/2
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)

"""Implement a function recursivly to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the
iterative code in the instructions."""


def get_fib(position):
    if position == 0 or position == 1:
        return position
    return get_fib(position - 1) + get_fib(position - 2)



# Test cases
print get_fib(9)
print get_fib(11)
print get_fib(0)



"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    pivot_pos = len(array) - 1
    pivot = array[pivot_pos]

    for i, v in enumerate(array[:pivot_pos]):
        if v > pivot:
            array.append(v)
            del array[i]
    return array

def swap(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp

#test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
#print quicksort(test)


def match(pattern, text):
    """cde, abcdefghi
        1234567, 345
    """
    patt_ind = 0
    patt_len = len(pattern)
    txt_ind = 0
    txt_len = len(text)
    while patt_ind < patt_len and txt_ind < txt_len:
        if pattern[patt_ind] == text[txt_ind]:
            patt_ind += 1
            if patt_ind == patt_len:
                return True
        else:
            patt_ind = 0

        txt_ind +=1

    return False



def test_match():
    print match('def', '')
    print match('1234567', '123')


test_match()