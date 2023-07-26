from sqlalchemy import Column, Integer, String, TEXT, ForeignKey
from database import Base


class MissionModel(Base):
    __tablename__ = 'missions'
    id = Column(String, primary_key=True)
    name = Column(String, nullable=True)


class RocketModel(Base):
    __tablename__ = 'rockets'
    id = Column(String, primary_key=True)
    name = Column(String, nullable=True)
    cost = Column(Integer, nullable=True)
    description = Column(TEXT, nullable=True)


class LaunchModel(Base):
    __tablename__ = 'launches'
    id = Column(String, primary_key=True)
    details = Column(TEXT, nullable=True)
    mission_id = Column(String, ForeignKey('missions.id'), nullable=False)
