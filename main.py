from game.generator import generate_answer
from game.logic import judge
from game.validator import validate_input
from utils.display import show_result, show_message
from rich.console import Console
from rich.table import Table
from rich import print

def main():
    answer = generate_answer()
    turn = 1
    history = []

    table = Table(title="Numeron")
    table.add_column("Turn", justify="right", style="cyan", no_wrap=True)
    table.add_column("Guess", style="magenta")
    table.add_column("EAT", style="yellow")
    table.add_column("BITE", style="green")

    while True:
       
        user_input = input("数字を入力: ")
        
        valid, msg =  validate_input(user_input)
        if not valid:
            show_message(msg)
            continue
        
        guess = list(user_input)
        eat, bite = judge(answer, guess)

        show_result(eat, bite)

        history.append(f"ターン:{turn} | {user_input} | {eat}EAT | {bite}BITE")
        table.add_row(
            str(turn), 
            user_input, 
            str(eat),
            str(bite)
        )
        console = Console()
        console.print(table)


        turn += 1
        if eat == 3:
            show_message(f"正解!! {turn}回でクリア")
            break


if __name__ == "__main__":
    main()