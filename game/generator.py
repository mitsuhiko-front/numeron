import random

def generate_answer():
    numbers = ["0123456789"]
    random.shuffle(numbers)
    return numbers[:3]
