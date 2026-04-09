from fastapi import FastAPI
from pydantic import BaseModel
from env import BusEnv

app = FastAPI()
env = BusEnv()

class Action(BaseModel):
    type: str

@app.post("/reset")
def reset():
    state = env.reset()
    return {
        "observation": {
            "time": state.time,
            "buses": [bus.dict() for bus in state.buses],
            "passenger_location": state.passenger_location,
            "destination": state.destination
        }
    }

@app.post("/step")
def step(action: Action):
    state, reward, done, _ = env.step(action.dict())

    return {
        "observation": {
            "time": state.time,
            "buses": [bus.dict() for bus in state.buses],
            "passenger_location": state.passenger_location,
            "destination": state.destination
        },
        "reward": float(reward),
        "done": bool(done)
    }

@app.get("/health")
def health():
    return {"status": "ok"}
