
def doMain(s):

    res = ''
    if s is None or len(s) == 0:
        return res
    for i in range(len(s)):
        j = i - 1
        k = i + 1
        tmp = s[i]
        while k < len(s) and s[k] == s[i]:
            tmp = tmp + s[k]
            k += 1
        while j >= 0 and k < len(s) and s[j] == s[k]:
            tmp = s[j] + tmp + s[k]
            j -= 1
            k += 1
        print(tmp)
        if len(tmp) > len(res):
            res = tmp
    # print (res)
    return res



if __name__ == '__main__':
    s='adada'
    doMain(s)