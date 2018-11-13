
def doMain(s):

    maxStr = ''
    tempStr = ''
    if len(s) in (0, 1):
        print (s)
        return s
    for item in s:
        if item not in tempStr:
            tempStr += item
        else:
            tempStr += item
            splitStr = tempStr[tempStr.index(item):]                                                                    
            if len(maxStr) < len(splitStr):
                maxStr = splitStr                                   
            # tempStr = tempStr[tempStr.index(item)+1:]
    if maxStr == '':
        maxStr = s[0]
    print (maxStr)



if __name__ == '__main__':
    s='abcda'
    doMain(s)