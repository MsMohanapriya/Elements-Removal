def ElementRemval(array):
    array.sort(reverse=True)
    cost=0
    for i in range(len(array)):
        cost+=array[i]*(i+1)
    return cost
    
array=list(map(int,input('enter elements: ').split()))
print(ElementRemval(array))