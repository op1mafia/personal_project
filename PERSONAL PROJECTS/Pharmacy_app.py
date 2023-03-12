
name = input("the name of medcine is ...")
price = input("the price of medcine is ...")
expiry_time = input("the expiry_time of medcine is ...")

Medcine = [name ,price ,expiry_time]
print(Medcine)

print("your data saved!!")

name1 = input("the name of medcine is ...")
price1 = input("the price of medcine is ...")
expiry_time1 = input("the expiry_time of medcine is ...")

Medcine1 = [name1 ,price1 ,expiry_time1]
print(Medcine1)

    
txt = input("enter the name of any medcine :")
if txt == Medcine[0]:
    print(Medcine)
elif txt == Medcine1[0]:
    print(Medcine1)

