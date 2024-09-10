n = float(input("enter data usage in (GB) :"))

if 0.0 < n <= 1.0:
    print ("your charge is 250$")
elif 1.0 < n <= 2.0:
    print("your charge is 500$")
elif 2.0 < n <= 5.0:
    print("your charge is 1000$")
elif 5.0 < n <= 10.0:
    print("your charge is 1500$")
elif n > 10.0:
    print("your charge is 2000$")
else:
    print ("bad data")
