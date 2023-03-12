import random 
import time

 
def random_num():

    
    i = 0
    while i in range(5):
        i = i + 1

        choices = random.randint(0,10)
        of = time.sleep(3)
        
        
        times = 0    
        while times <= 3:
            num = int(input("enter a number start in 0 and finish in 10 :___"))
            if num == choices:
                print("sucess")
                print("you win the game gg")
                i = 5
            elif num >= choices:
                print("the number is a big number")
                times = times + 1

            elif num <= choices:
                print("the number is a mini number")
                times = times + 1

            else:
                print("error")

            if times == 3:
                print("you lose the game")
                i = 5    
            

print(random_num())