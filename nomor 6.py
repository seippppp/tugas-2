x,y = map (float, input("enter x and y cordinate : ").split())

if x > 0 and y > 0:
    print ("is in quadrant I")
elif x < 0 and y > 0:
    print ("is in quadrant II")
elif x < 0 and y < 0:
    print ("is in quadrant III")
elif x > 0 and y < 0:
    print ("is in quadrant IV")
elif y == 0:
    print ("is on the x-axis")
elif x == 0:
    print ("is on the y-axis")