from fastapi import APIRouter, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from functions.fun_attention import Attention

router = APIRouter(prefix="/attention", 
                    tags=["attention"],
                    responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

LETTER = 'letra'
QUANTITY = 'cantidad'
NUQUANTITY = 3

@router.get("/")
async def attention():
    letter = Attention.getLetter()
    board = Attention.getBoardLetter(letter,NUQUANTITY)   
    #quantity_letter = Attention.getQuantityLetter(board,letter)
    board[LETTER] = letter 
    board[QUANTITY] = NUQUANTITY 
    return board

