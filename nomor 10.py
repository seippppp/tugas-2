bread_type = input ("bread type (w / s): ").strip().lower()
dough = input ("are you using double loaf size (yes / no): ").strip().lower()
manual = input ("are you cooking this manual or not (yes / no): ").strip().lower()

if manual == "no":
    if bread_type == "w":
        if dough == "no":
            print("Primary Kneading --> 15 minutes")
            print("Primary rising --> 60 minutes")
            print("Secondary Kneading --> 18 minutes")
            print("Secondary Rising --> 20 minutes")
            print("loaf shaping --> 2 seconds")
            print("final rising --> 75 minutes")
            print("Baking --> 45 minutes")
            print("Cooling --> 30 minutes")
        if dough == "yes":
            print("Primary Kneading --> 22.5 minutes")
            print("Primary rising --> 90 minutes")
            print("Secondary Kneading --> 27 minutes")
            print("Secondary Rising --> 30 minutes")
            print("loaf shaping --> 3 seconds")
            print("final rising --> 112.5 minutes")
            print("Baking --> 67.5 minutes")
            print("Cooling --> 45 minutes")
    if bread_type == "s":
        if dough == "no":
            print("Primary Kneading --> 20 minutes")
            print("Primary rising --> 60 minutes")
            print("Secondary Kneading --> 33 minutes")
            print("Secondary Rising --> 30 minutes")
            print("loaf shaping --> 2 seconds")
            print("final rising --> 75 minutes")
            print("Baking --> 35 minutes")
            print("Cooling --> 30 minutes")
        if dough == "yes":
            print("Primary Kneading --> 30 minutes")
            print("Primary rising --> 90 minutes")
            print("Secondary Kneading --> 49.5 minutes")
            print("Secondary Rising --> 45 minutes")
            print("loaf shaping --> 3 seconds")
            print("final rising --> 112.5 minutes")
            print("Baking --> 52.5 minutes")
            print("Cooling --> 45 minutes")

if manual == "yes":
    if bread_type == "w":
        if dough == "no":
            print("Primary Kneading --> 15 minutes")
            print("Primary rising --> 60 minutes")
            print("Secondary Kneading --> 18 minutes")
            print("Secondary Rising --> 20 minutes")
            print("loaf shaping --> 2 seconds")
            print("remove the dough for manual baking")
        if dough == "yes":
            print("Primary Kneading --> 22.5 minutes")
            print("Primary rising --> 90 minutes")
            print("Secondary Kneading --> 27 minutes")
            print("Secondary Rising --> 30 minutes")
            print("loaf shaping --> 3 seconds")
            print("remove the dough for manual baking")
    if bread_type == "s":
        if dough == "no":
            print("Primary Kneading --> 20 minutes")
            print("Primary rising --> 60 minutes")
            print("Secondary Kneading --> 33 minutes")
            print("Secondary Rising --> 30 minutes")
            print("remove dough for manual baking")
        if dough == "yes":
            print("Primary Kneading --> 30 minutes")
            print("Primary rising --> 90 minutes")
            print("Secondary Kneading --> 49.5 minutes")
            print("Secondary Rising --> 45 minutes")
            print("loaf shaping --> 3 seconds")
            print("remove dough for manual baking")