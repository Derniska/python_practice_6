def selection_sort(arr):
    for i in tqdm(range(0,len(arr)-1)):
        cur_min_ind = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[cur_min_ind]:
                cur_min_ind = j
        arr[i], arr[cur_min_ind] = arr[cur_min_ind], arr[i]
        
def selection_sort_t(arr):
    start = time.time()
    selection_sort(arr)
    finish = time.time()
    time_com = selection_sort_t
    return time_com