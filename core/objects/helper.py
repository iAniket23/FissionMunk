# Event Dispatcher
# Probability
import random

# Generate a random number between the given range
def get_probability(range=(0, 1000)):
    prob = random.randint(range[0], range[1])
    return prob//range[1]