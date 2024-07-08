my_dict = {'Sasha' : 1994,'Danil': 1995,'Lena': 1993}
print(my_dict)
print(my_dict.get('Sasha'))
print(my_dict.get('Katya'))
my_dict.update({'Sergey': 1988,
               'Anton': 1978})
print(my_dict)
del my_dict['Lena']
print(my_dict.get('Lena'))
print(my_dict)


my_set = {1,1,1,2,2, 'banana', True}
print(my_set)
my_set = {1,1,1,2,2, 'banana', True, "apple",False}
print(my_set)
print(my_set.discard(1))
print(my_set)