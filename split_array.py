# arr = [1,2,3,4,5,6,7,8]

# def split_array(arr, numOfSubarray):
#     l = len(arr) // numOfSubarray
#     new_arr = []
#     res_arr = []
#     new_l = l
#     prev_l = 0
    
   

#     while new_l <= len(arr):
        
#         for i in range(prev_l, new_l):

#             new_arr.append(arr[i])
        
            
#         res_arr.append(new_arr)
#         prev_l = new_l
#         new_l = prev_l + len(arr) // numOfSubarray
#         new_arr = []
    
#     return res_arr

# print(split_array(arr,8))

    













arr = [1,2,3,4,5,6,7,8]

def split_array(arr, numOfSubarray):
    l = len(arr) // numOfSubarray
    print(l)
    remainder = len(arr) % numOfSubarray
    print(remainder)
    res_arr = []
    prev_l = 0
    
   


        
    for _ in range(numOfSubarray):
        extra = 1 if remainder > 0 else 0
        remainder -= 1
        print("remainder",remainder)
        new_l = prev_l + l +  extra

        res_arr.append(arr[prev_l:new_l])
        prev_l = new_l
            
    return res_arr

print(split_array(arr,3))

    



