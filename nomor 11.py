substance = float(input("enter celcius substance: "))

if 100 * 0.95 <= substance <= 100 * 1.05:
    print("the substance is WATER")
elif 357 * 0.95 <= substance <= 357 * 1.05:
    print("the substance is MERCURY")
elif 1187 * 0.95 <= substance <= 1187 * 1.05:
    print("the substance is COPPER")
elif 2193 * 0.95 <= substance <= 2193 * 1.05:
    print("the substance is SILVER")
elif 2660 * 0.95 <= substance <= 2660 * 1.05:
    print("the substance is GOLD")
else:
    print("substamce unknown")