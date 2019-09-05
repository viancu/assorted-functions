import random
import time
"""
Function to determine whether a sorted array A contains at least one element,
A[i], such that A[i] = i.

Examples: A = [-1, 1, 2, 4, 5, 7, 9, 18] will return true
          A = [-1, 0, 1, 3, 5, 14] will return false
"""

def contains_i_help(arr, offset):
    if len(arr) == 1:
        if arr[0] == offset:
            return True
        else:
            return False
    half = len(arr)//2
    left = arr[:half]
    left_offset = offset
    right = arr[half:]
    right_offset = half + offset

    if left_offset >= left[0]:
        left_bool = contains_i_help(left, left_offset)
    else:
        left_bool = False
    if right_offset >= right[0]:
        right_bool = contains_i_help(right, right_offset)
    else:
        right_bool = False
    return left_bool or right_bool

def contains_i(arr):
    return contains_i_help(arr, 0)

def contains_i_iter(arr):
    i = 0
    for elem in arr:
        if elem == i:
            return True
        i+=1
    return False

def compare_contains_i():
    k = [i + 1 for i in range(0, 100000)]
    i = random.randint(1, 100000)
    k[i] = i
    start = time.time()
    contains_i(k)
    end = time.time()
    time1 = end - start
    print(time1)
    start = time.time()
    contains_i_iter(k)
    end = time.time()
    time2 = end - start
    print(time2)
    print("This many times faster:", time2 / time1)






