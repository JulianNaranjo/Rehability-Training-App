import random

ABECEDARIO = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 
'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

SIZE_BOARD = 250


class Attention:

    def getBoardLetter():
        board : list = list()
        dic_board: dict = dict()
        for idletter in range (SIZE_BOARD):        
            #board.append(random.choice(ABECEDARIO))
            dic_board[idletter] = random.choice(ABECEDARIO)
            #dic_board = dict([(idletter,random.choice(ABECEDARIO))])
        return dic_board
        #return board

    def getLetter(dic_board):
        letter : str
        letter = random.choice(dic_board)       
        #dic_board[LETTER] = letter
        #print(dic_board)
        return letter 
    
    def getQuantityLetter(dic_board, letter):
        return list(dic_board.values()).count(letter)

        
    #def getLetter(board):
        #letter : str
        #letter = random.choice(board)
        #print(letter)
        #return letter 

"""
lista = Attention.getBoardLetter()
print (lista)
letra = Attention.getLetter(lista)
print(letra)
cantidad = Attention.getQuantityLetter(lista,letra)
print (cantidad)
"""


    