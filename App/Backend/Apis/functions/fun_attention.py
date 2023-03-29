import random

ABECEDARIO = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 
'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

SIZE_BOARD = 100
ONE = 1

class Attention:

    def getLetter():
        letter : str
        letter = random.choice(ABECEDARIO)       
        return letter 

    def getBoardLetter(letter, quantity):
        ABECEDARIO.remove(letter)
        dic_board = {}
        sort_position = random.sample(range(ONE, SIZE_BOARD+ONE), SIZE_BOARD)
        for idx, pos in enumerate(sort_position):
            if idx < quantity:
                dic_board[pos] = letter
            else:
                dic_board[pos] = random.choice(ABECEDARIO)
        dic_board_sort = dict(sorted(dic_board.items()))
        return dic_board_sort

    #Obtener cantidad de letras, en revision
    #def getQuantityLetter(dic_board, letter):
    #    return list(dic_board.values()).count(letter)

#diccionario = Attention.getBoardLetter('A', 2)
#print(diccionario)

    