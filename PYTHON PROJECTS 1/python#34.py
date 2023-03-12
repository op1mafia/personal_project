# r r+ w w+ a a+
files = open("S_file.txt", "a+")
print(files.write("\nnassim"))
files.close()

files = open("S_file2.txt", "a+")
print(files.write("\nnassim"))
files.close()

files = open("S_file.html", "a+")
print(files.write("<h1>saad</h1>"))
files.close()