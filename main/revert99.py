for i in range(9, 0, -1):
    for j in range(9, 0, -1):
        k = i*j
        print(f"{i:2d}*{j:2d}={k:2d}", end="")
    print()
