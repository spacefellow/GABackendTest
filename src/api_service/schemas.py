from pydantic import BaseModel


class RocketSchema(BaseModel):
    rocket_id: str
    rocket_name: str
    rocket_cost: int
    rocket_description: str


class LaunchSchema(BaseModel):
    launch_id: str
    launch_details: str


class MissionSchema(BaseModel):
    mission_id: str
    mission_name: str
