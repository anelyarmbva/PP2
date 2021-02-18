a = str(input("Введите первое значение: " ))
b = str(input("Введите второе значение: " ))
what = input("Выберите один из символов: " )

if what == '+':
    c = a + b
    print(str(c))
elif what == '-':
    c = a - b
    print(str(c))
else: 
    print("Вы не выбрали неправильную операцию!")