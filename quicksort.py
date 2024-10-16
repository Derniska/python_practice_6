# A quick sort algorithm
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()
        left_arr = []
        right_arr = []
        for item in arr:
            if item < pivot:
                left_arr.append(item)
            else:
                right_arr.append(item)
    return quick_sort(left_arr) + [pivot] + quick_sort(right_arr)
def quick_sort_t(arr):
    start = time.time()
    quick_sort(arr)
    finish = time.time()
    time_comp = finish - start
    return time_comp
