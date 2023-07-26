from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, update, func
from database import get_async_session
from api_service.models import MissionModel

router = APIRouter()


@router.get('/missions')
async def get_all_missions(session: AsyncSession = Depends(get_async_session)):
    """
    Эндпойнт для получения всех миссий
    """
    query = select(MissionModel)
    result = await session.execute(query)
    return result.scalars().all()


@router.get('/mission/{id}')
async def get_one_mission(id: str, session: AsyncSession = Depends(get_async_session)):
    """
    Эндпойнт для получения одной из миссий по полю id
    """
    result = await session.execute(select(MissionModel).filter_by(id=id))
    return result.scalars().all()


@router.get('/missions/count')
async def get_all_launches(session: AsyncSession = Depends(get_async_session)):
    """
    Эндпойнт для получения количества миссий
    """
    query = select(MissionModel)
    result = await session.execute(query)
    return {'Number of missions': len(result.scalars().all())}
