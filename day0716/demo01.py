height = float(input("请输入身高单位为:m "))
weight = float(input("请输入体重额单位为:kg "))
bmi = weight / pow(height, 2)
print("您的BMI指数: ", bmi)
if bmi < 18.5:
    print("您的体重过轻")
if bmi >= 18.5 and bmi < 24.9:
    print("正常范围注意保持")
if bmi >= 24.9 and bmi < 29.9:
    print("过重了")
if bmi > 29.9:
    print("肥胖")
"""
asdiajsd
adsjl'
dasj
"""
