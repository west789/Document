def CanGenerate(letters, word):
    max_x = len(letters[0])
    max_y = len(letters)
    first_letter = word[0]
    for i in range(len(max_y)):
        for j in range(len(max_x)):
            if letters[i][j] == first_letter:
                return BFS_word(letters, word, i, j)
    return False

def BFS_word(letters, word, i, j):
    word_list = [letters[i][j]]
    que = []
    while len(word_list)<=word:
        if i > 0:
            pass

letters = [ ['A', 'R', 'E'],['I', 'P', 'D'],['E', 'L', 'P'] ]
word = "ARE"
word = "APPLE"
word = "AIR"
CanGenerate(letters, word)