immutable_var = tuple([10,11,12])
print(immutable_var)
immutable_var[0] = 20
print(immutable_var)
#ошибка выдается по причине того, что элементы кортежа не могут быть изменены, изменения возможны только при условии, что в элементы кортежа будет добавлен список и уже внутри него мы можем производить изменения


mutable_list = ['piano','violin','bass']
print(mutable_list)
mutable_list[1]= 'guitar'
print(mutable_list)