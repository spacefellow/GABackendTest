from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, update, func
from database import get_async_session
from api_service.models import LaunchModel

router = APIRouter()


@router.get('/launches')
async def get_all_launches(session: AsyncSession = Depends(get_async_session)):
    """
    Эндпойнт для получения всех пусков
    """
    query = select(LaunchModel)
    result = await session.execute(query)
    return result.scalars().all()


@router.get('/launch/{id}')
async def get_one_launch(id: str, session: AsyncSession = Depends(get_async_session)):
    """
    Эндпойнт для получения одного из пусков по полю id
    """
    result = await session.execute(select(LaunchModel).filter_by(id=id))
    return result.scalars().all()


@router.get('/launches/count')
async def get_all_launches(session: AsyncSession = Depends(get_async_session)):
    """
    Эндпойнт для получения количества пусков
    """
    query = select(LaunchModel)
    result = await session.execute(query)
    return {'Number of launches': len(result.scalars().all())}
