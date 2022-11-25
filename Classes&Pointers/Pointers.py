# num 1 = 11
# num 2 = num1 

num1 = 11 

num2 = num1 

print('Before num 2 value is updated:')
print('num1=', num1)
print('num2=', num2)

print('\nnum1 points to:', id(num1)) #points to address where num1 and num2 are located
print('num2 points to:', id(num2)) #points to the same address in memory

num2 = 22 #changed value

print('\nAfter num2 is updated:')
print('num1=', num1)
print('num2=', num2)

print('\nnum1 points to:', id(num1)) #num1 is still the same location in memory
print('num2 points to:', id(num2)) #num2 is now a new location in memory

#Integers are immutable - cannot be changed 
#Once that number is in memory - it doesn't change, you can point to a different integer that is stored 
#somewhere else but you can't actually change the number once you create it