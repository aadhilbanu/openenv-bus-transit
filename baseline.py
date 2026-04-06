from env import BusEnv
from grader import evaluate

env = BusEnv()
state = env.reset()

total_reward = 0
time_taken = 0

for _ in range(50):
    action = {"type": "wait"}

    for bus in state.buses:
        if abs(bus.location - state.passenger_location) < 2:
            action = {"type": "board"}

    state, reward, done, _ = env.step(action)

    total_reward += reward
    time_taken += 1

    if done:
        break

easy_score = evaluate("easy", state=state, reward=total_reward)
medium_score = evaluate("medium", time=time_taken)
hard_score = evaluate("hard", time=time_taken, seats=5)

print("Easy Score:", easy_score)
print("Medium Score:", medium_score)
print("Hard Score:", hard_score)
