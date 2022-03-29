import math
import random

rand_100 = random.sample(range(1000), 100)
print(rand_100)


# 計算數列平均值
def f_ave(f_num):
    ave = sum(f_num) / 100
    # print(ave)
    return ave


mean = f_ave(rand_100)
print(mean)


# 增加計算標準差功能
def decorated(func):
    def wrapper_ave(*args):
        func(*args)
        print("執行後新增功能：")
        var = sum((l - mean) ** 2 for l in rand_100) / 100
        std_dev = math.sqrt(var)
        # print(std_dev)
        return std_dev
    return wrapper_ave
    # var = sum((l - mean) ** 2 for l in rand_100) / 100
    # var = sum((l-mean)**2 for l in list) / len(list)


f_ave = decorated(f_ave)
dev = f_ave(rand_100)
print(dev)

# 驗算
mean1 = sum(rand_100) / 100
var1 = sum((l-mean)**2 for l in rand_100) / 100
st_dev1 = math.sqrt(var1)
print("驗算結果: \n" + "平均數 = " + str(mean1) + "\n" + "標準差 = " + str(st_dev1))
