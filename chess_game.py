import time


def make_move(opponent_name, move_number):
    time.sleep(1)
    print(f'{opponent_name.upper()} is making MOVE {move_number} against LARRY') 
    time.sleep(.1)
    print(f'LARRY is making MOVE {move_number} against {opponent_name.upper()}') 
    
def play_game(opponent_name):
    for move_number in range(1, 6):
        make_move(opponent_name, move_number)

    print(f'\n DONE GAME against {opponent_name} \n\n')

start_time = time.time()

play_game('mortal 1')
play_game('mortal 2')
play_game('mortal 3')

total_time = time.time() - start_time
print(f"Total time taken: {total_time:.2f} seconds")