def insert_at_end(array,UB,n,array_max,element):
    if UB==array_max-1:
        print("Insertion not possible")
        return UB
    
    UB=UB+1
    array[UB]=element
    n=n+1
    return UB,n

array_max=5
array=[10,20,30,40,None]
UB=3
n=4

UB, n=insert_at_end(array,UB,n,array_max,50)
print("Full array after inserting the element:",array)


