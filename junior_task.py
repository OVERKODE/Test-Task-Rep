# ЗАДАНИЕ: Простое математическое приложение (Калькулятор)
# Напишите программу, которая выполняет базовые математические операции:
# +, -, *, /
# Программа должна запрашивать у пользователя два числа и операцию, а затем выводить результат.

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

print("Отлично! Числа получены. Теперь выберите действие (+, -, *, /): ")

action = input()

if action == "+":
    print("Ответ: ", a + b)
elif action == "-":
    print("Ответ: ", a - b)
elif action == "*":
    print("Ответ: ", a * b)
elif action == "/" and b != 0:
    print("Ответ: ", a / b)
elif action == "/" and b == 0:
    print("На 0 делить нельзя")

else:
    print("Такого действия нет в программе")