#Numbers
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max_num(12,27,2))

def min_num(num1, num2, num3):
    if num1 <= num2 and num1 <= num3:
        return num1
    elif num2 <= num1 and num2 <= num3:
        return num2
    else:
        return num3
print(min_num(32,48,17))

#string
def match_string(str1, str2):
    if str1 == str2:
        print("the strings go match")
    else:
        print("the string dont match")
match_string("saad", "saade")