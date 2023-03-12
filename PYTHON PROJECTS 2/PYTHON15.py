is_hungry = True
wants_to_eat = True

if is_hungry or wants_to_eat:
    print("go eat you are hungry or you just want to eat")
elif is_hungry and not wants_to_eat:
    print("eat so you can survive ")
elif not is_hungry and wants_to_eat:
    print("do not eat you are not hungry")
else:
    print("do not eat")
