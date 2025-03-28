def merge(left,right):
    res=[]
    i=0
    j=0

    while i<len(left) and j<len(right):

        if left[i] <right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
        res.extend(left[i:])
        res.extend(right[j:])
        return res
        
def merge_sort(arr):
    mid=len(arr)//2

    left=arr[:mid]
    right=arr[mid:]

    left=merge_sort(left)
    right=merge_sort(right)

    return merge(left,right)




arr=[12, 3,6,1,9,15,11,10]
sorted_arr = merge_sort(arr)
print(sorted_arr)