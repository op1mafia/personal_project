def names(saad,ahmed,mohamed):
    if saad > ahmed and saad > mohamed:
        return saad
    if ahmed > saad and saad > mohamed:
        return ahmed
    else:
        return mohamed
print(names(80,40,50))