num1 = input("請輸入乘數: ")
num2 = input("請輸入被乘數: ")
num1 = int(num1)
num2 = int(num2)

for i in range(1, num1+1):
    print(f"\n")
    for j in range(1, num2+1):
        print(f"{j} * {i} = {i*j}".ljust(10) ,end="  ")

num3 = round(1.23556, 2)
print(num3)
