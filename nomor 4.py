warna = input("enter first letter of color: ").strip().lower()

if warna == "o":
    print("the contents of a compressed-gas cylinder is AMMONIA")
elif warna == "b":
    print ("the contents of a compressed-gas cylinder is CARBON MONOXIDE")
elif warna == "y":
    print ("the contents of a compressed-gas cylinder is HYDROGEN")
elif warna == "g":
    print ("the contents of a compressed-gas cylinder is OXYGEN")
else:
    print("Contents unknown")