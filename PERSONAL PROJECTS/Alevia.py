#dialogue1
def question_answer(dialog):
#englesh
    if dialog == 'hi':
        print('Alevia :hi')
    
    elif dialog == 'hello':
        print('Alevia :hello')
    
    elif dialog == "what's your name?":
        print('Alevia :my name is Alevia')
    
    elif dialog == 'how old are you?':
        print('Alevia :i dont know because i am robot')
    
    elif dialog == 'do you speak french?':
        print('Alevia :oui je parle la langue   française')
    
    elif dialog == 'how are you?':
        print('Alevia :i am fine')
    
    elif dialog == 'do you have a parents?':
        print('Alevia :no because i am robot')
        
        
    elif dialog == 'hi':
        print('Alevia :hi')
    
    elif dialog == 'hello':
        print('Alevia :hello')
    
    elif dialog == "what's your name":
        print('Alevia :my name is Alevia')
    
    elif dialog == 'how old are you':
        print('Alevia :i dont know because i am robot')
    
    elif dialog == 'do you speak french':
        print('Alevia :oui je parle la langue   française')
    
    elif dialog == 'how are you':
        print('Alevia :i am fine')
    
    elif dialog == 'do you have a parents':
        print('Alevia :no because i am robot')
    
#french 
    elif dialog == 'bonjours':
        print('Alevia :bonjours')
    
    elif dialog == 'salut':
        print('Alevia :salut')
    
    elif dialog == "comment tu t'appelle?":
        print("Alevia :je m'appelle Alevia")
    
    elif dialog == 'quel âge avez vous?':
        print('Alevia :je ne sais pas car je    suis un robot')
    
    elif dialog == "parles-tu l'anglais?":
        print('Alevia :Yes, i speak englesh')    
    
    elif dialog == 'ça va?':
        print('Alevia :Oui, je vais bien')
    
    elif dialog == 'as–tu des parents?':
        print('Alevia :Non, car je suis un robot')
        
        
    elif dialog == 'bonjours':
        print('Alevia :bonjours')
    
    elif dialog == 'salut':
        print('Alevia :salut')
    
    elif dialog == "comment tu t'appelle":
        print("Alevia :je m'appelle Alevia")
    
    elif dialog == 'quel âge avez vous':
        print('Alevia :je ne sais pas car je    suis un robot')
    
    elif dialog == "parles–tu l'anglais":
        print('Alevia :Yes, i speak englesh')    
    
    elif dialog == 'ça va':
        print('Alevia :Oui, je vais bien')
    
    elif dialog == 'as–tu des parents':
        print('Alevia :Non, car je suis un robot')

    else:
        print('Alevia :je ne sais pas ce mot')

def calculator():

    num1 = float(input("Alevia :enter first number: "))
    operator = input('Alevia :enter operator: ')


    if operator == "+":
         num2 = float(input("Alevia :enter second number: "))
         print(num1+num2)
         
    elif operator == "-":
         num2 = float(input("Alevia :enter second number: "))
         print(num1-num2)
         
    elif operator == "×":
         num2 = float(input("Alevia :enter second number: "))
         print(num1*num2)
         
    elif operator == "/":
         num2 = float(input("Alevia :enter second number: "))
         print(num1/num2)
         
    elif operator == "#2":
         print(num1**num1)
         
    elif operator == "#3":
         print(num1*num1*num1)
         
    else:
         print('error')


dialog0 = input("_______please say pls dialog for question or pls math for a calculatation_____:")


if dialog0 == 'pls math':
    print(calculator())
 
elif dialog0 == 'pls dialog':
    dialog1 = input()
    print(question_answer(dialog1))
    
    dialog2 = input()
    print(question_answer(dialog2))
    
    dialog3 = input()
    print(question_answer(dialog3))
    
    dialog4 = input()
    print(question_answer(dialog4))
    
    dialog5 = input()
    print(question_answer(dialog5))
    
    
else:
    print('error')