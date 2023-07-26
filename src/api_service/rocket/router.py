from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, update, func
from database import get_async_session
from api_service.models import RocketModel

router = APIRouter()


@router.get('/rockets')
async def get_all_rockets(session: AsyncSession = Depends(get_async_session)):
    """
    Эндпойнт для получения всех ракет
    """
    query = select(RocketModel)
    result = await session.execute(query)
    return result.scalars().all()


@router.get('/rocket/{id}')
async def get_one_rocket(id: str, session: AsyncSession = Depends(get_async_session)):
    """
    Эндпойнт для получения одной из ракет по полю id
    """
    result = await session.execute(select(RocketModel).filter_by(id=id))
    return result.scalars().all()


@router.get('/rockets/count')
async def get_all_launches(session: AsyncSession = Depends(get_async_session)):
    """
    Эндпойнт для получения количества ракет
    """
    query = select(RocketModel)
    result = await session.execute(query)
    return {'Number of rockets': len(result.scalars().all())}
