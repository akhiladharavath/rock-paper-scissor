import random

def winner(user,robo):
    if user==robo:
        print("Draw")
    elif (user=='rock' and robo=='scissor') or (user=='paper' and robo=='rock') or (user=='scissor' and robo=='paper'):
        print("you won")
    else:
        print("you lost")

while True:
    choices = ['rock','paper','scissor']
    robo = random.choice(choices)
    user = input("Enter rock, paper, or scissors ").lower()
    if user not in choices:
        print("Invalid choice. Please enter rock, paper, or scissors")
        continue
    print('Robo choice :', robo)
    winner(user,robo)
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break