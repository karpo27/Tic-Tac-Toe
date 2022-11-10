import table
import secrets

av_options = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
g_op = ["", "", "", "", "", "", "", "", ""]

def start_intro():
    print("Welcome to Tic Tac Toe game!\n"
          "")
    rules = input("if you already know the rules press 'Enter' otherwise type 'help'. ")

    if rules in ['help', 'HELP', 'Help']:
        print("1. The game is played on a grid that's 3 squares by 3 squares.\n"
              "2. You are 'X' or 'O' (depends on your choice) and the AI uses the remaining option.\n"
              "3. Players take turns putting their marks in empty squares. Squares are identified with numbers:\n"
              f"{table.example_table}"
              "4. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.\n"
              "5. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.")

def select_name():
    name = input("\n"
                 "Please enter your name: ")
    print(f"Hello {name}!")

def select_difficulty():
    game_dif = input(f"Please select the AI\'s difficulty level:\n"
                 f"1- Easy\n"
                 f"2- Medium\n"
                 f"3- Hard\n"
                 f"")

    if game_dif not in ["1", "2", "3"]:
        print("Please select a valid option ")
        select_difficulty()

def select_mark():
    global p_mark
    p_mark = input("Choose 'X' or 'O' ""(remember 'X' moves first)\n"
                     "")

    x_choice = ["x", "X", "1"]
    o_choice = ["o", "O", "0", "2"]

    if p_mark not in x_choice + o_choice:
        print("Please select a valid option ")
        select_mark()

    if p_mark in x_choice:
        p_mark = "X"
        global ai_mark
        ai_mark = "O"
        play_player()
    else:
        p_mark = "O"
        ai_mark = "X"
        play_ai()

def play_player():
    if len(av_options) == 9:
        print(table.table.format(g_op[0], g_op[1], g_op[2], g_op[3], g_op[4], g_op[5], g_op[6], g_op[7], g_op[8]))

    p_choice = input(f"Choose an empty square from the list {av_options}: ")

    if p_choice in av_options:
        av_options.remove(p_choice)
        g_op.pop(int(p_choice) - 1)
        g_op.insert(int(p_choice) - 1, p_mark)
    else:
        print("Please select a valid option ")
        play_player()

    print(table.table.format(g_op[0], g_op[1], g_op[2], g_op[3], g_op[4], g_op[5], g_op[6], g_op[7], g_op[8]))
    play_ai()

def play_ai():
    ai_choice = secrets.choice(av_options)
    print(ai_choice)

    av_options.remove(ai_choice)
    g_op.pop(int(ai_choice) - 1)
    g_op.insert(int(ai_choice) - 1, ai_mark)

    print(table.table.format(g_op[0], g_op[1], g_op[2], g_op[3], g_op[4], g_op[5], g_op[6], g_op[7], g_op[8]))
    play_player()

def win():

    if len(av_options) == 4:
        if g_op[0] == g_op[1] and g_op[0] == g_op[2] and (g_op[0], g_op[1], g_op[2]) != ("", "", ""):




start_intro()
select_name()
select_difficulty()
select_mark()

