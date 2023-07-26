import requests
from api_service.models import RocketModel, LaunchModel, MissionModel
from fastapi import Depends
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_async_session

URL = "https://spacex-production.up.railway.app"


async def insert_launches_and_missions_data(model_list: list([MissionModel, LaunchModel]),
                                            current_session: AsyncSession = Depends(get_async_session)):
    """
    Добавление данных пусков и миссий в базу данных
    """
    query_launches = """
    query Launches {
      launches {
        id
        details
        mission_id
        mission_name
      }
    }
    """
    launches = requests.post(URL, json={'query': query_launches}).json()['data']['launches']
    for launch in launches:
        stmt_1 = insert(model_list[0]).values(
            id=launch['mission_id'][0],
            name=launch['mission_name'],
        ).on_conflict_do_nothing()
        stmt_2 = insert(model_list[1]).values(
            id=launch['id'],
            details=launch['details'],
            mission_id=launch['mission_id'][0],
        ).on_conflict_do_nothing()
        await current_session.execute(stmt_1)
        await current_session.execute(stmt_2)
        await current_session.commit()
    print('launches and missions added')


async def insert_rockets_data(rocket_model: RocketModel,
                              current_session: AsyncSession = Depends(get_async_session)):
    """
    Добавление данных ракет в базу данных
    """
    query_rockets = """
    query Rockets {
      rockets {
        id
        name
        cost_per_launch
        description
      }
    }
    """
    rockets = requests.post(URL, json={'query': query_rockets}).json()['data']['rockets']
    for rocket in rockets:
        stmt = insert(rocket_model).values(
            id=rocket['id'],
            name=rocket['name'],
            cost=rocket['cost_per_launch'],
            description=rocket['description'],
        ).on_conflict_do_nothing()
        await current_session.execute(stmt)
        await current_session.commit()
    print('rockets added')


async def fill():
    """
    Прогон функций добавления данных в базу данных
    """
    func_list = [
        (insert_launches_and_missions_data, [MissionModel, LaunchModel]),
        (insert_rockets_data, RocketModel),
    ]
    for func in func_list:
        async for session in get_async_session():
            await func[0](func[1], session)


def main():
    """
    Главная функция
    """
    import asyncio
    asyncio.run(fill())


main()
