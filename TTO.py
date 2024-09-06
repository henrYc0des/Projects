import time
import random


def play_game():
    print("| 0 | 1 | 2 |\n| 3 | 4 | 5 |\n| 6 | 7 | 8 |\n")
    allowed_inputs = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    #numbs will be replaceds with x and o here
    grid_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    while True:
        p_square_num, grid_list = player_turn(grid_list, allowed_inputs)
        print(f"X makes a move to square {p_square_num}")
        print(format_grid(grid_list))
        print("")

        won = win_checker("X", grid_list)
        if won == True:
            print(f"X HAS WON THE MATCH!!!")
            break
        tie = tie_checker(grid_list)
        if tie == True:
            print("THE GAME HAS TIED!!!")
            break
        #       #       #       #       #       #       #       #
        c_square_num, grid_list = computer_turn(grid_list)
        time.sleep(1)
        print(f"O makes a move to square {c_square_num}")  
        print(format_grid(grid_list))
        print("")
        
        won = win_checker("O", grid_list)
        if won == True:
            print(f"O HAS WON THE MATCH!!!")
            break
        tie = tie_checker(grid_list)
        if tie == True:
            print("THE GAME HAS TIED!!!")
            break


# player is X
def player_turn(grid_list, allowed_inputs):
    while True:
        try:
            player_input = int(input("X's turn. Input move (0-8): ")
    )
            if player_input not in allowed_inputs:
                print(f"'{player_input}' is not a valid input. ")
            elif player_input not in grid_list:
                print(f"'{player_input}' has already been taken. ")
            else:
                grid_list[player_input] = "X"
                return player_input, grid_list
        except ValueError:
            print(f"Your input must be a number (0-8)")

# computer is O
def computer_turn(grid_list):
    computer_grid_list = []
    for square in grid_list:
        if isinstance(square, int):
            computer_grid_list.append(square)
    computer_input = random.choice(computer_grid_list)

    grid_list[computer_input] = "O"
    return computer_input, grid_list

def win_checker(c, gl):
    #check all possilbe winning outcomes here
    win = (c, c, c)

    win_coditions = [
    (gl[0], gl[1], gl[2]),  # Horizontal top row
    (gl[3], gl[4], gl[5]),  # Horizontal middle row
    (gl[6], gl[7], gl[8]),  # Horizontal bottom row

    (gl[0], gl[3], gl[6]),  # Vertical left column
    (gl[1], gl[4], gl[7]),  # Vertical middle column
    (gl[2], gl[5], gl[8]),  # Vertical right column

    (gl[0], gl[4], gl[8]),  # Diagonal from top-left to bottom-right
    (gl[2], gl[4], gl[6])   # Diagonal from top-right to bottom-left
    ]  

    for win_codition in win_coditions:
        if win_codition == win:
            return True
    return False

def tie_checker(gl):
    for square in gl:
        num = isinstance(square, int)
        if num:
            return False
        
    return True
    
    
def format_grid(grid_list):
    forming_grid = ""
    for square in grid_list:
        forming_grid = f"{forming_grid}| {square} "
    forming_grid = forming_grid + "|"

    list_forming_grid = list(forming_grid)

    for i, square in enumerate(list_forming_grid):
        if square not in ("X", "O", "|", " "):
            list_forming_grid[i] = " "

    list_forming_grid[12] = "|\n|"  
    list_forming_grid[24] = "|\n|"  

    formatted_grid = ''.join(list_forming_grid)   
    return formatted_grid


play_game()