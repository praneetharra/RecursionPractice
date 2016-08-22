def printRev(a):
    if len(a)==1:
        return a
    else:
        return printRev(a[1:])+a[0]
        
print(printRev('asdfg'))
