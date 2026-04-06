import random
from models import EnvState, BusState

class BusEnv:
    def __init__(self):
        self.reset()

    def reset(self):
        self.time = 0
        self.state = EnvState(
            time=0,
            buses=[
                BusState(bus_id=1, location=0, speed=8, seats_available=20),
                BusState(bus_id=2, location=-10, speed=12, seats_available=5)
            ],
            passenger_location=0,
            destination=50
        )
        return self.state

    def step(self, action):
        reward = 0.0
        done = False

        for bus in self.state.buses:
            traffic_factor = random.uniform(0.8, 1.2)
            bus.location += bus.speed * traffic_factor

        if action["type"] == "wait":
            reward -= 0.1

        elif action["type"] == "board":
            for bus in self.state.buses:
                if abs(bus.location - self.state.passenger_location) < 2:
                    if bus.seats_available > 0:
                        reward += 1.0
                        done = True
                    else:
                        reward -= 0.3

        elif action["type"] == "switch":
            reward -= 0.2

        reward -= 0.01 * self.time

        self.time += 1
        self.state.time = self.time

        return self.state, max(0.0, min(1.0, reward)), done, {}

    def state(self):
        return self.state
