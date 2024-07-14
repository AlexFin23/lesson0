list_ = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
while list_[0] >= 0:
    i = list_.pop(0)
    if i == 0:
        continue
    if len(list_) < 1:
        break
    print(i)




