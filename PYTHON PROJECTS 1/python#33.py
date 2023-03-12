files = open("S_file.txt", "r")
for lista in files.readlines():
    print(lista)
files.close()