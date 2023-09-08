num = int(input("Enter integer (0 for output): "))
sum = 0
while num != 0:
    
    for i in range(num+1):
       sum += i
       print(f"{i} sum is {sum}")
               
    num = int(input("Enter integer (0 for output): "))
    print(sum)

# num = int(input("Enter the integer (0 to 100): "))
# sum = 0
# i = 1
# while i <= num:
#     print(i)
#     sum += i
#     i = i + 1
#     print(f"sum is {sum}")
    
# print(f"Sum is {sum}, {i}")