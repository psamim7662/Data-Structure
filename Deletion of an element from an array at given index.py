def delete_at_given_index(arr,index):
    if index<0 & index>=len(arr):
        print("Insertion not possible or wrong index")
        return arr
    for i in range(index,len(arr)-1):
        arr[i]=arr[i+1]
    arr.pop()
    return arr
arr=[1,3,4,42,65]
print("Array after deletion of last elelment:",delete_at_given_index(arr.copy(),2))