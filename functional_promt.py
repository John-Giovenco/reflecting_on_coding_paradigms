def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

flatten_and_sort()

"""How does this solution ensure data immutability?

    - This is an append only data base so data can never be deleted or added. 

    Is this solution a pure function? Why or why not?

    - Yes, because it will return the same argument values and will not be able to be modified. 
   
    Is this solution a higher order function? Why or why not?
    
    - I think it is because it uses the built in "sorted" function with in the function. 
    
    Would it have been easier to solve this problem using a different programming style?
    
    - Yes, I think the built in flatten function could have been used.
    
    Why in particular is functional programming a helpful paradigm when solving this problem?
    
    - Because it makes us think about the problem a bit deeper then we would have to if we used OOP."""