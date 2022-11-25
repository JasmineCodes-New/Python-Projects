#O(1) at the end of the list
#append & pop - adding on to the end of the list and removing from end of list
#simple operations - O(1)


#O(n) - n is number of items in list at the front of the list
#ex: my_list.pop(0) or my_list.insert(0,11)
#pop(0) - pop at index of 0 and have to reindex
#insert(0,11) - insert at index of 0 the number 11 and have to reindex list


#O(n) - middle of the list 
#ex: my_list.insert(1, 'Hi') in the middle of the list
#insert & remove from middle of the list - reindex list


#O(n)
#Looping through a list for a number 


#O(1)
#Looking by index - can go directly to that place in memory


# Most efficient to least efficient in order
    # O(1) - constant 
    # O(log n) - divide and conquer
    # O(n) - proportional to number of items
    # O(nlog n)
    # O(n2) - loop within a loop
