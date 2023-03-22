from fastapi import APIRouter, HTTPException, status
from functions.fun_attention import Attention
from pydantic import BaseModel

#uvicorn users:app --reload
router = APIRouter(prefix="/attention", 
                    tags=["attention"],
                    responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

#pipenv shell

#class Board(BaseModel):
#    id : int
#    letter : str

LETTER = 'letra'
QUANTITY = 'Cantidad'

#@router.get("/",response_model=list[Board])
@router.get("/")
async def attention():
    board = Attention.getBoardLetter()
    letter = Attention.getLetter(board)
    quantity_letter = Attention.getQuantityLetter(board,letter)
    board[LETTER] = letter 
    board[QUANTITY] = quantity_letter 
    return board

