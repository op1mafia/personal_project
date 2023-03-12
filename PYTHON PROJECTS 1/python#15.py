SX = [1,2,3]
SZ = [4,5,6]
SA = [2,6,4,9,1,3]
SV = [3,2,5,8,0,7]
SD = ["saad","oumaima","nassim"]
SC = ["saad play in computer"]

SX.append("welcome to marrakesh")
SX.extend(SZ)
SZ.insert(0,"paloza, menara")
SA.sort()
SV.sort(reverse=True)
SD.remove("saad")
SC.clear()

print(SX)
print(SZ)
print(SA)
print(SV)
print(SD)
print(SC)