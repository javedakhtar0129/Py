weight = int(input("Input your weight(in pounds): "))
print(f"Your weight is: {weight}")

type = input("\nNow \n(L)bs OR (K)gs: ")

if type=="L" or type=="l" or type=="Lbs" or type=="lbs":
    print(f"Your weight in LBS is {float(weight)*0.45}")
elif type=="K" or type=="k" or type=="Kg" or type=="kg":
    print(f"Your weight in LBS is {float(weight)/100}")


