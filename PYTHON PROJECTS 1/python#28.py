secret_answer = "rabat"
answer = ""
count = 0
limit = 3
lose = False
while secret_answer != answer and not lose:
    if count < limit:
        answer = input("what is capital of morocco? ")
        count += 1
    else:
        lose = True

if lose:
    print("you lose")
else:
    print("you won")