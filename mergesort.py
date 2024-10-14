import random
random.seed = 42
my_list1 = random.sample(range(100), k=30)
my_list2 = random.sample(range(1000000), k=150000)
my_list3 = random.sample(range(10000), k = 1025)

def merge_sort(arr):
    if len(arr) > 1:
    #     Splitting the array in half
        part1 = arr[:len(arr)//2]
        part2 = arr[len(arr)//2 :]
    #     Recursively calling the algorith on each part
        merge_sort(part1)
        merge_sort(part2)
    #     i and j to keep track of left and right parts
        i=j=k=0 
        while i < len(part1) and j < len(part2):
            if part1[i] < part2[j]:
                arr[k] = part1[i]
                i +=1
            else:
                arr[k] = part2[j]
                j +=1
            k +=1
#         Adding the only element left in the right or left chunk
        while i < len(part1):
            arr[k] = part1[i]
            i +=1
            k +=1
        while j < len(part2):
            arr[k] = part2[j]
            j +=1
            k +=1
print(f'The unsorted array is: \n{my_list1}.')
merge_sort(my_list1)
print(f'The sorted array is: \n {my_list1}')

def timer_merge_sort(arr):
    start = time.time()
    merge_sort(arr)
    finish = time.time()
    time_complex = finish - start
    print(time_complex)