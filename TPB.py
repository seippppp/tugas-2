number = int(input())

status = True
i = 0
for i in range(2, number):
    if number % i == 0:
        status = False
if status:
    print("IT IS  A PRIME NUMBER")
else:
    print("IT IS NOT A PRIME NUMBER")