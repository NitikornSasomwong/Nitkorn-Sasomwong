x = float(input("imput your score:"))

if (x>=80 and x<=100):
    print("get A")
elif (x>=75and x<=79):
    print("get B+")
elif (x>=70and x<=74):
    print("get B")
elif (x>=65 and x<=69):
    print("get c+")
elif (x>=60 and x<=64):
    print("get c")
elif (x>=55 and x<=59):
    print("get D+")
elif (x>=50 and x<=54):
    print("get D")
elif (x>=0 and x<=49):
    print("get F")
else:
    print("error")
