def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)

def picnic(items,leftwidth,rightwidth):
    print('ITEMS'.center(leftwidth+rightwidth,'-'))
    for i , j in items





items={'chocolates':10, 'cakes' : 20, 'drinks':15}

picnic(items,10,5)
picnic(items,5,10)