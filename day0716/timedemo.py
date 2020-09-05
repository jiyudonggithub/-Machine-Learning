import time

t = time.localtime()
print(time.strftime("%Y{}%m{}%d{} %H:%M:%S", t).format("年", "月", "日"))
