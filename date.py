import datetime
x=datetime.datetime.now()
print(x.strftime("%A %I:%M:%S %p %d-%m-%Y day of the year:%j week of the year:%U"))
a=input("plane name:")
if(a=="SPANTHIPHYLLUM"):
    print("Yes - Spathiphyllum is the best plant ever!")
elif(a=="spathiphyllum"):
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not [input]!")