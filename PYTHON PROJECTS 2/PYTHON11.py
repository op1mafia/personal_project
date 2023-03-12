codezilla =  ["programming", "python", "php", "html", "css"]

tutorial = ["extend", "list1", "codezilla"]

langue = ["python", "css", "processing"]

alphabet = ["sq", "ed", "fy"]

codezilla.extend(tutorial)
print(codezilla)

tutorial += codezilla
print(tutorial)

langue.append("java")
print(langue)

langue.insert(1, "php")
print(langue)

langue.remove("css")
print(langue)

langue.pop()
print(langue)

variable = langue.pop()
print(variable)

print(langue.index("python"))

print(langue.count("python"))


alphabet.sort()
print(alphabet)

new_list = alphabet.copy()
print(new_list)
