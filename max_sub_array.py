"""
Find the maximum possible contiguous sub-array of an array.
TODO: Make the couldbe_arr get rid of possible arrays that 
      are known to be shorter in length.
"""

def max_sub_array(arr):
    i = 0
    # Just an arr carrying the maximum possible contiguous array
    curr_arr = []
    couldbe_arr = []
    # An array of arrays that could possibly be the max sub array.
    curr_arr.append(arr[0])
    curr_sum = arr[0]
    while i < (len(arr) - 1):
        if len(arr) <= 1:
            return arr
        # First option: the sum of the array is negative.
        if curr_sum < 0:
            if (arr[i+1] >= 0) or (curr_sum < arr[i+1]):
                curr_arr = [arr[i+1]]
                curr_sum = arr[i+1]
            else:
                couldbe_arr.append(list(curr_arr))
                curr_arr = [arr[i+1]]
                curr_sum = arr[i+1]
        # Second option: the sum of the array is positive.
        else:
            if arr[i+1] > 0:
                curr_arr.append(arr[i+1])
                curr_sum += arr[i+1]
            elif (curr_sum + arr[i+1]) > 0:
                couldbe_arr.append(list(curr_arr))
                curr_arr.append(arr[i+1])
                curr_sum += arr[i+1]
            else:
                couldbe_arr.append(list(curr_arr))
                curr_arr = [arr[i+1]]
                curr_sum = arr[i+1]
        i += 1
    couldbe_arr.append(curr_arr)
    max_arr = couldbe_arr[0]
    max_sum = sum(couldbe_arr[0])
    for sub_arr in couldbe_arr:
        sum_sub = sum(sub_arr)
        if sum_sub > max_sum:
            max_arr = sub_arr
            max_sum = sum_sub
    print(couldbe_arr)
    print('\n')
    return max_arr
