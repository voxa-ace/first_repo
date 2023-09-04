print('Hello World!')

print("Hello Git")

fruit = 'apple'
for char in fruit:
    print(char)

a = 1
while a <= 5:
    a = a + 1
    print(a)

a = 0
while True:
    a = a + 1
    print(a)
    if a >= 20:
        break

def say_hello():
    print("Hello World!")   # блок, що належить функції
    # кінець функції say_hello()

# виклик функції 
say_hello()

# ще один виклик ф-ції
say_hello()

def print_max(a, b):
    if a > b:
        print(a, "максимально")
    elif a == b:
        print(a, "дорівнює", b)
    else:
        print(b, "максимально")
    
print_max(3, -2) # пряма передача змінних

x = 7
y = 10
print_max(x, y) # передача змінних у якості аргументів

def plus(a, b):
    c = a + b
    return c
res = plus(8, 45)
print(res)

def plus(a, b):
    return a + b
print(plus(12, 4))

x = 50

def func():
    global x
    print("x дорівнює", x)   # x дорівнює 50
    x = 2
    print("Змінюємо глобальне значення x на", x)    # змінюємо глобальне значення x на 2

func()
print("Значення x складає", x)  # Значення x складає 2

