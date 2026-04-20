import random

def generate_answer():
    numbers = ["0123456789"]
    random.shuffle(numbers)
    return numbers[:3]

def judge(answer, guess):
    eat = 0
    bite = 0

    for i in range(len(answer)): 
        if answer[i] == guess[i]:
            eat += 1
        elif guess[i] in answer:
            bite += 1
    return eat, bite

    






