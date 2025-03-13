def delete_at_beginning(array):
    if len(array)==0: 
        print("Invalid index or deleltion not possible")
        return array
    for i in range(len(array)-1):
        array[i]=array[i+1]
    array.pop()
    return array
array=[1,2,3,4,4]
print("The array after deletion of first element:",delete_at_beginning(array.copy()))