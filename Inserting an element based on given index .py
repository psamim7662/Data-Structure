def insert_at_index(array,UB,n,i,element,array_max):
    if UB==array_max-1:
        print("Inesertion not possible")
        return UB
    for k in range(UB,i-1,-1):
        array[k+1]=array[k]
    array[i]=element
    
    UB=UB+1
    n=n+1
    
    return UB,n
array_max=7
array=[10,20,30,None]
UB=2
n=3
i=3
element=25
UB,n=insert_at_index(array,UB,n,i,element,array_max)
print("Full array after insertion:",array)