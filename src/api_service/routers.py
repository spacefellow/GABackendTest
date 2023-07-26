from fastapi import APIRouter
from api_service.launch.router import router as launch_router
from api_service.rocket.router import router as rocket_router
from api_service.mission.router import router as mission_router


aggregated_router = APIRouter()

routers = (
    launch_router,
    rocket_router,
    mission_router,
)

for router in routers:
    aggregated_router.include_router(
        router,
    )