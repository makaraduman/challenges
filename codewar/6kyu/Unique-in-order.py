def unique_in_order(iterable):
    newList = []
    for i in iterable:
        if newList == []: # if the newList is empty
            newList.append(i) # Add the first item to the list
        elif newList[-1] != i: # if the list item in the list is not equal to i:
            newList.append(i) # Add i to the list 
    return newList

    pass
