import random

def generate_answer():
    numbers = list("0123456789")
    random.shuffle(numbers)
    return numbers[:3]
