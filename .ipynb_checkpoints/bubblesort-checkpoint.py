# The simplest sorting algorithm
def bubble_sort(arr):
    for i in tqdm(range(len(arr))):
        swap = False
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
        if not swap:
                break
    return arr

def bubble_sort_t(arr):
    start = time.time()
    bubble_sort(arr)
    finish = time.time()
    time_com = finish - start
    return time_com