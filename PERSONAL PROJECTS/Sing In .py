print("please creat a new email")

name1 = input("enter your first name: ")
name2 = input("enter your last name:")
email = name1 +"_"+ name2 +"@gmail.com"
print(email)

password = input("enter password: ")

retryE = input("retry your email: ")
retryP = input("retry your password: ")


if email == retryE and password == retryP:
    print("welcome "+name1)

elif email == retryE and password != retryP:
    print("invalide password, please retry")

elif email != retryE and password == retryP:
    print("invalide email, please retry")

else:
    print("please retry")
    