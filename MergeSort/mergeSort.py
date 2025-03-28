arr=[12, 3,6,1,9,15,11,10]

def merge(left, right):
    result_arr=[]

    i=0
    j=0

    while i < len(left) and j <len(right):
        if left[i] <= right[j]:
            result_arr.append(left[i])
            i+=1
        
        else:
            result_arr.append(right[j])
            j+=1
        
    # Add any remaining items from left
    result_arr.extend(left[i:])
    
    # Add any remaining items from right
    result_arr.extend(right[j:])    
    return result_arr


def merge_sort(arr):

    if len(arr) <=1:
        return arr
    
    mid = len(arr)//2 

    left =  arr[:mid]
    right = arr[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left,right)
sorted_arr = merge_sort(arr)
print(sorted_arr)