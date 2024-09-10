total_purchase = float(input("enter total purchase: "))
student = input("are you a student (yes / no): ").strip().lower()

if student == "yes":
    total_purchase = total_purchase * 0.80
    total_akhir = "{:.2f}".format (total_purchase * 1.05)
    print (total_akhir)
elif student == "no":
    total_akhir = "{:.2f}".format(total_purchase * 1.05)
    print (total_akhir)
else:
    print ("please try again use the format (yes / no)")
