# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    i = j = 0
    index = 0

    # TO-DO
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            # print("This is arrA index", arrA[i])
            merged_arr[index] = arrA[i]
            i += 1
        else:
            merged_arr[index] = arrB[j]
            j += 1
        
        index += 1
    while i < len(arrA):
        merged_arr[index] = arrA[i]
        i += 1
        index += 1
    while j < len(arrB):
        merged_arr[index] = arrB[j]
        j += 1
        index += 1
        
    print(merged_arr)
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) < 2:
      return arr
    else:
      m = int(len(arr)/2)
      arr1 = merge_sort(arr[:m])
      arr2 = merge_sort(arr[m:])
        
      return merge(arr1, arr2)

    


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
