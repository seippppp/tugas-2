weekday = float(input("enter total minutes on weekdays: "))
night = float(input("enter total minutes on night time (8 p.m. to 7 a.m.): "))
weekend = float(input("enter total minutes on weekdays: "))

total_time = weekday + night + weekend

if weekday < 600:
    pretax = 39.99
    avg_min_cost = "{:.2f}".format(total_time / pretax)
    tax = float("{:.2f}".format(pretax * 0.0525))
    bill = float("{:.2f}".format(pretax + tax))

else:
    extra_time = weekday % 600
    pretax = float("{:.2f}".format(39.99 + (extra_time * 0.40)))
    avg_min_cost = float("{:.2f}".format(total_time / pretax))
    tax = float("{:.2f}".format(pretax * 0.0525))
    bill = float("{:.2f}".format(pretax + tax))

print(f"pretax bill {pretax}$")
print(f"total average minutes cost {avg_min_cost}")
print(f"total tax {tax}$")
print(f"total bill {bill}$")