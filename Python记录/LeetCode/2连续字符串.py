import copy

def doMain(s):
    """
    :type s: str
    :rtype: int
    """
    # 解法1

    # strDict = {}
    # currentMax = 0
    # maxLength = 0
    # for i in range(len(s)):
    #     if s[i] in strDict and i-strDict[s[i]]-1<=currentMax:
    #         if maxLength < currentMax:
    #             maxLength = currentMax
    #         currentMax = i - strDict[s[i]] - 1
    #     currentMax += 1
    #     print(maxLength)
    #     print (currentMax)
    #     strDict[s[i]] = i
    #     print (strDict)
    # print (maxLength if maxLength > currentMax else currentMax)
    # return (maxLength if maxLength > currentMax else currentMax)

    # 解法2
    if not s:
        return 0
    longest_str = 1
    substr=''
    for item in s:
        if item not in substr:
            substr += item
        else:
            if len(substr) > longest_str:
                longest_str = len(substr)
            substr += item
            substr = substr[substr.index(item)+1:]
        print (substr)
    if len(substr) > longest_str:
        longest_str = len(substr)                
    return longest_str

if __name__ == '__main__':
    s='pwdfwke'
    doMain(s)