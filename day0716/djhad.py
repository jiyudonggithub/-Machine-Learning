# num = 100
# while num < 1000:
#     b = int(num / 100)
#     s = int(num / 10 % 10)
#     g = int(num % 10)
#     sum = b ** 3 + s ** 3 + g ** 3
#     if num == sum:
#         print(num)
#     num += 1
# print("结束")
num = 10000
while num < 100000:
    sum = int(str(num)[::-1])
    if sum == num:
        print(num)
    num += 1
print("结束")
print(type(sum))