num = int(input("Enter integer (0 for output): "))
sum = 0
while num != 0:
    for i in range(num):
        sum += i
    break
    num = int(input("Enter integer (0 for output): "))