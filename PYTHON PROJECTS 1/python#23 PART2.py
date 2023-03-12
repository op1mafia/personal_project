email = "x@gmail.com"
password = 1234
if email == "x@gmail.com" and password == 1234:
   print("welcome")

elif email == "x@gmail.com" and password != 1234:
     print("invalid password please try again")

elif email != "x@gmail.com" and password == 1234:
     print("invalid email please try again")
else:
     print("please try again")