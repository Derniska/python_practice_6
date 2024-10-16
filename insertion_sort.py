# An implementation of insertion_sort algorithm
def insertion_sort(arr):
    for i in tqdm(range(1,len(arr))):
        j = i 
        while arr[j-1] > arr[j] and j > 0:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
def insertion_sort_t(arr):
    start = time.time()
    insertion_sort(arr)
    finish = time.time(arr)
    time_comp = finish - start