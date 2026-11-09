def while_numbers():
    i = 1
    n = int(input("Введіть ціле число n: "))
    while i <= n:
        print(i)
        i += 1

while_numbers()


def multiplication_table(n):
    print(f"Таблиця множення для числа {n}:")
    for j in range(1, 11):
        print(f"{n} x {j} = {n * j}")
user_number = int(input("Введіть ціле число: "))

multiplication_table(user_number)

def for_numbers():
    n = int(input("Введіть ціле число n: "))
    for i in range(1, n + 1):
        print(i)

for_numbers()
