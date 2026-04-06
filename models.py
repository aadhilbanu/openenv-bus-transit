from pydantic import BaseModel
from typing import List

class BusState(BaseModel):
    bus_id: int
    location: float
    speed: float
    seats_available: int

class EnvState(BaseModel):
    time: int
    buses: List[BusState]
    passenger_location: float
    destination: float

class Action(BaseModel):
    type: str  # wait / board / switch
