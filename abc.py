import random
print("ROCK PAPER SCISSOR GAME")        
def generate_computers_choice():
    random_num = random.randint(1,3)
    if random_num == 1:
        return 'rock'
    elif random_num == 2:
        return 'paper'
    else:
        return 'scissors'

def is_user_choice_valid(choice):
    return choice == 'rock' or choice == 'paper' or choice == 'scissors'
    
def get_new_user_choice(choice):
    while choice != 'rock' and choice != 'paper' and choice != 'scissors':
          print('That is not a valid choice.')
          choice = input('\nEnter rock, paper, or scissors: ')
    return choice

def did_player_win(player, comp):
    if player == 'rock' and comp == 'scissors':
        return True
    elif player == 'scissors' and comp == 'paper':
        return True
    elif player == 'paper' and comp == 'rock':
        return True
    else:
        return False
3
comp_choice = generate_computers_choice()
user_choice = input('Enter rock, paper, or scissors: ')
if not is_user_choice_valid(user_choice):
    user_choice = get_new_user_choice(user_choice)

while user_choice == comp_choice:
    print('\nComputer\'s choice:', comp_choice)
    print('You\'ve tied.  Choose again.')
    
    comp_choice = generate_computers_choice()
    user_choice = input('\nEnter rock, paper, or scissors: ')
    if not is_user_choice_valid(user_choice):
        user_choice = get_new_user_choice(user_choice)

print('\nComputer\'s choice:', comp_choice)
if did_player_win(user_choice, comp_choice):
    print('Congrats! You win.')
else:
    print('Too bad. Better luck next time!')
