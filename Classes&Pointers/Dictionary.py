#dictionaries are used to store data in key:value pairs
#a dictionary is a collection which is ordered, changeable, and do not allow duplicates
#duplicate vales will overwrite existing values 

dict1 = {
    'value': 11
}

dict2 = dict1

print('Before value is updated:')
print('dict1 =', dict1)
print('dict2 =', dict2)

print('\ndict1 points to:', id(dict1))
print('dict2 points to:', id(dict2)) #points to the same location in memory