number = int(input("Please input a number (4~9): "))

# 第一種星星
for i in range(0, number+1):
    print('*' * i)

# 第二種星星
for i in range(0, number+1):
    print(' ' * (number-i) + '*' * i)

# 第三種星星
for i in range(0, number+1):
    print(' ' * (number-i) + '*' * (2*i-1))

# 第四種星星
for i in range(0, number+1):
    print(' ' * (number-i) + '*' * (2*i-1))
for i in range(number-1, 0, -1):
    print(' ' * (number-i) + '*' * (2*i-1))
