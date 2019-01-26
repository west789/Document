import copy

count = 0
resultList = [1, 2, 5, 10]

# def doTask(coinList, reaminMoney):
#     if reaminMoney == 0:
#         print(coinList)
#         return
#     elif reaminMoney < 0:
#         return
#     else:
#         for item in resultList:
#             coinListNew = copy.copy(coinList)
#             coinListNew.append(item)
#             remainMoney1 = reaminMoney - item
#             doTask(coinListNew, remainMoney1)

def doTask(coinList, remainMoney):
    if remainMoney == 0:
        print(coinList)
        global count
        count += 1
        return
    elif remainMoney <0:
        return
    else:
        for item in resultList:
            resultListNew = copy.copy(coinList)
            resultListNew.append(item)
            doTask(resultListNew, remainMoney-item)


if __name__ == '__main__':
    coinList = []
    remainMoney = 10
    doTask(coinList, remainMoney)
    print(count)
