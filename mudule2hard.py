n = int(input("Введите пароль: "))
password = ""
for first_number in range (1, n):
    for second_number in range (first_number +1, n):
        if n % (first_number + second_number) == 0:
            password += str(first_number)
            password += str(second_number)

print(password)