from game.generator import generate_answer
from game.logic import judge
from game.validator import validate_input
from utils.display import show_result, show_message

def main():
    answer = generate_answer()
    turn = 0
    
    while True:
        turn += 1
        user_input = input("数字を入力: ")
        
        valid, msg =  validate_input(user_input)
        if not valid:
            show_message(msg)
            continue
        
        guess = list(user_input)
        eat, bite = judge(answer, guess)

        show_result(eat, bite), show_message()

        if eat == 3:
            show_message(f"正解!! {turn}回でクリア")
            break


if __name__ == "__main__":
    main()