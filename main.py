from game.generator import generate_answer
from game.logic import judge
from game.validator import validate_input
from utils.display import show_result, show_message

def main():
    answer = generate_answer()
    user_input = input("数字を入力: ")

    valid, msg =  validate_input(user_input)
    if not valid:
        return show_message(msg)
    
    guess = list(user_input)
    eat, bite = judge(answer, guess)

    return show_result(eat, bite), show_message("ppppp")



if __name__ == "__main__":
    main()