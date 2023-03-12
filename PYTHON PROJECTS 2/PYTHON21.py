def power (base_Num, pow_Num):
    result = 1
    for index in range(pow_Num):
        result =result*base_Num
    return result

print(power(3,3))