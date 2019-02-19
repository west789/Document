def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    resultList = []
    row = len(matrix)
    col = len(matrix[0]) if row>0 else 0
    
    totalNums = col*row
    i = 0
    while len(resultList)<totalNums:
        for rightCol in range(i, col-i):
            resultList.append(matrix[i][rightCol])
        downRow = -1
        for downRow in range(i+1, row-i):
            resultList.append(matrix[downRow][rightCol])
        if downRow == -1:
            break
        leftCol = -1
        for leftCol in range(rightCol-1, -1+i, -1):
            resultList.append(matrix[downRow][leftCol])
        if leftCol == -1:
            break
        for upRow in range(downRow-1, i, -1):
            resultList.append(matrix[upRow][leftCol])
        
        i += 1
    return resultList
    print(resultList)

if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    print(matrix)
    spiralOrder(matrix)
