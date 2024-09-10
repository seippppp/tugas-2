berat = float(input("enter berat badan (dalam pounds): "))
tinggi = float(input("enter tinggi badan (dalam inch): "))

BMI = float("{:.1f}".format (703 * berat / tinggi ** 2))

if BMI <= 18.5:
    print ("you are UNDERWEIGHT")
elif BMI <= 24.9:
    print ("you are NORMAL")
elif BMI <= 29.9:
    print ("you are OVERWEIGHT")
elif BMI >= 30.0:
    print ("you are OBESE")