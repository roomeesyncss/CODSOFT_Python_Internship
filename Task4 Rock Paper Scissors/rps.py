import random
import tkinter as tk
import ttkbootstrap as ttkbs

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ___)___
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ___)___
          ______)
       __________)
      (____)
---.__(___)
'''

ascii_img = [rock, paper, scissors]
choices = ["Rock", "Paper", "Scissors"]
player_score = 0
comp_score = 0

start_frame = None  # Initialize start_frame as a global variable
main_frame = None  # Initialize main_frame as a global variable


def determine_winner(user_choice):
    global player_score, comp_score

    comp_choice = random.randint(0, 2)
    comp_img_label.config(text=ascii_img[comp_choice])

    if user_choice == comp_choice:
        result_label.config(text="It's a draw!")
    elif (user_choice == 0 and comp_choice == 2) or \
            (user_choice == 1 and comp_choice == 0) or \
            (user_choice == 2 and comp_choice == 1):
        result_label.config(text="You win!")
        player_score += 1
    else:
        result_label.config(text="You lose!")
        comp_score += 1

    score_label.config(text=f"Your score: {player_score}, Computer score: {comp_score}")


def rock_selected():
    determine_winner(0)


def paper_selected():
    determine_winner(1)


def scissors_selected():
    determine_winner(2)


def start_game():
    start_frame.pack_forget()
    main_frame.pack()


def replay_game():
    global player_score, comp_score
    player_score = 0
    comp_score = 0
    main_frame.pack_forget()  # Hide the main game frame
    start_frame.pack()  # Show the start frame


def main():
    global start_frame, main_frame
    root = tk.Tk()
    root.title("Rock, Paper, Scissors Game")

    style = ttkbs.Style(theme="superhero")

    start_frame = ttkbs.Frame(root, padding="20")
    start_frame.pack(fill="both", expand=True)

    start_label = ttkbs.Label(start_frame, text="ROCK PAPER SCISSORS GAME", font=("Helvetica", 20))
    start_label.pack(pady=30)

    start_button = ttkbs.Button(start_frame, text="Start Game", command=start_game)
    start_button.pack()


    main_frame = ttkbs.Frame(root, padding="10")

    rock_button = ttkbs.Button(main_frame, text="Rock", command=rock_selected)
    rock_button.pack(side="left", padx=10, pady=10)

    paper_button = ttkbs.Button(main_frame, text="Paper", command=paper_selected)
    paper_button.pack(side="left", padx=10, pady=10)

    scissors_button = ttkbs.Button(main_frame, text="Scissors", command=scissors_selected)
    scissors_button.pack(side="left", padx=10, pady=10)

    global comp_img_label, result_label, score_label
    comp_img_label = tk.Label(main_frame, text="", font=("Courier", 14))
    comp_img_label.pack(pady=20)

    result_label = ttkbs.Label(main_frame, text="", font=("Courier", 14))
    result_label.pack()

    score_label = ttkbs.Label(main_frame, text="Your score: 0, Computer score: 0", font=("Courier", 12))
    score_label.pack(pady=10)

    replay_button = ttkbs.Button(main_frame, text="↺", command=replay_game, style="danger.TButton")
    replay_button.pack(side="left", padx=10, pady=10)


    main_frame.pack_forget()

    root.mainloop()


if __name__ == "__main__":
    main()