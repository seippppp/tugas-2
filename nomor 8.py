print("(1) first free service")
print("(2) second free service")

service_number = int(input("enter the free service number: "))
miles = int(input("enter number of miles:"))

if service_number == 1:
    if 1500 < miles <= 3000:
        print ("vehicle must be serviced.")
    else:
        print ("not in the range of the first free service")
elif service_number == 2:
    if 3001 < miles <= 4500:
        print ("vehicle must be serviced.")
    else:
        print ("not in the range of the second free service")