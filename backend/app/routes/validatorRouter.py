from fastapi import APIRouter
from app.services.validateService import check

router = APIRouter()

@router.post( "/" )
async def validate( data : dict ):
    return await check( data )