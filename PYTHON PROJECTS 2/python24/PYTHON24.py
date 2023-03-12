saad_file = open("saad24.txt", "r")
for line in saad_file.readlines():
    print(line + " is cool")
saad_file.close()