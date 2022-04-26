number = int(input("Please input a number (4~9): "))
print("\n")

for i in range(number, 0, -1):
    print(' ' * (number-i) + '*' * (2*i-1))
