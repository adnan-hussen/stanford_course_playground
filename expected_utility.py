import random

def simulate_game():
    total_reward = 0

    while True:
        total_reward += 4

        probability = random.random()

        if probability <= 1/3:
            return total_reward
        else:
            continue


sum_reward = 0
for _ in range(10000000):
    sum_reward += simulate_game()

print(sum_reward/10000000)