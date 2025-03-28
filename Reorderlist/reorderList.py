arr=[1,2,3,4,5,6,7]


res_arr=[]

def reorderList(arr):
    beginning=0
    ending=len(arr)-1
    
    while beginning <= ending and len(res_arr)!=len(arr):

        if beginning == ending:
            res_arr.append(arr[beginning])

    
        else:
            res_arr.append(arr[beginning])
            res_arr.append(arr[ending])
        beginning+=1        
        ending-=1
       


    return res_arr

print(reorderList(arr))

