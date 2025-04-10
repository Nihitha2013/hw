x=(input("Enter your character : "))
if len(x)==0:
    print("Enter only one character for check")
elif (x>="a" and x<="z") or (x>="A" and x<="Z"):
        print("Its an alphabet")
elif x.isnumeric():
        print("It is a Number")
else:
        print("Its not an alphabet")