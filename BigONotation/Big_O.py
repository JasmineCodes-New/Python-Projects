#o(n) - O of (n)
def print_items(n):
    for i in range(n): 
        print(i)


print_items(10)


#o(2n) - simplified to O of (n) - drop constants 
def print_1items(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)


print_1items(10)


#o(n2) - O of (n2) - nested for loop
def print_items2(n):
    for i in range(n):
        for j in range(n):
            print(i, j)


print_items2(10)


#o(n3) - O of (n3) simplified down to O of (n2) - n4, n5, etc. all simplified to O of (n2)
def print_items3(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i, j, k)


print_items3(10)


#nested for loop + separate loop - drop non-dominants :  O(n2) + O(n) = O(n2) : dropped O(n)
def print_items4(n):
    for i in range(n):
        for j in range(n):
            print (i, j)

    
    for k in range(n):
        print(k)


print_items4(10)


#O(1) - constant : as n increases, the number of operations is going to remain constant - most efficient Big O
def add_items(n): 
    return n + n


add_items(10)


#O(log n) - log 8 = 3 : 2 to the third power = 8 - 3 steps in dividing list, dividing it again, and finding number

#O(n logn) - Merge Sort & Quick Sort

#Most efficient in order
    #O(1)
    #O(log n)
    #O(n)
    #O(nlog n)
    #O(n2)


#function with 2 paramaters - O (a + b) : can't simplify further - different terms for input 
def print_items5(a, b): #O(a)
    for i in range(a):
        print(i)

    
    for i in range(b): #O(b)
        print(i)

print_items5(10, 10)

