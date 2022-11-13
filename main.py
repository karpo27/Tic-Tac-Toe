import table
import secrets

av_options = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
g_op = ["", "", "", "", "", "", "", "", ""]
turn = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
AI_LIST = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def start():
    print("\n"
          "Welcome to Tic Tac Toe game!\n"
          "")
    rules = input("If you already know the rules press any key to continue, otherwise type 'help'. ")

    if rules in ['help', 'HELP', 'Help']:
        print("\n"
              "1. The game is played on a grid that's 3 squares by 3 squares.\n"
              "2. You can choose 'X' or 'O' and the other person or AI uses the remaining option.\n"
              "3. Players take turns putting their marks in empty squares. Squares are identified with numbers:\n"
              f"{table.example_table}"
              "4. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.\n"
              "5. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.")

    select_name("1")


def select_name(n_player):
    if n_player == "1":
        global name_p1
        name_p1 = input("\n"
                     "Player 1 please enter your name: ")
        if name_p1 == "":
            name_p1 = "Mysterious Guy"

        print(f"\n"
              f"Hello {name_p1}!")

        global dictionary
        dictionary = {"1": name_p1}
        select_game_mode()
    else:
        global name_p2
        name_p2 = input("\n"
                        "Player 2 please enter your name: ")
        if name_p2 == "":
            name_p2 = "Mysterious Guy's partner"

        print(f"\n"
              f"Hello {name_p2}!")

        dictionary.update({"2": name_p2})
        select_mark()


def select_game_mode():
    global game_mode
    game_mode = input(f"\n"
                     "Please select the game mode:\n"
                     "1- Easy\n"
                     "2- Medium\n"
                     "3- Hard\n"
                      "4- PVP\n"
                      "")

    if game_mode not in ["1", "2", "3", "4"]:
        print("Please select a valid option ")
        select_game_mode()
    elif game_mode == "4":
        select_name("2")

    select_mark()


def select_mark():
    global p_mark
    global ai_mark
    p_mark = input("\n"
                   f"{name_p1} choose 'X' or 'O' ""(remember 'X' moves first)\n"
                   "")

    x_choice = ["x", "X", "1"]
    o_choice = ["o", "O", "0", "2"]

    if p_mark not in x_choice + o_choice:
        print("Please select a valid option ")
        select_mark()

    if p_mark in x_choice:
        p_mark = "X"
        ai_mark = "O"
        dictionary.update({"1": [name_p1, p_mark]})
        if game_mode == "4":
            dictionary.update({"2": [name_p2, ai_mark]})
            play_player("1")
        else:
            play_player("1")
    else:
        p_mark = "O"
        ai_mark = "X"
        dictionary.update({"1": [name_p1, p_mark]})
        if game_mode == "4":
            dictionary.update({"2": [name_p2, ai_mark]})
            play_player("2")
        else:
            play_ai(game_mode)


def play_player(n_player):
    if len(av_options) == 9:
        print("\n"
              f"    {dictionary[n_player][0]}'s Turn")
        print(table.table.format(g_op[0], g_op[1], g_op[2], g_op[3], g_op[4], g_op[5], g_op[6], g_op[7], g_op[8]))
    else:
        print(f"    {dictionary[n_player][0]}'s Turn")

    p_choice = input("\n"
                     f"Choose an empty square from the list {av_options}: ")

    if p_choice in av_options:
        av_options.remove(p_choice)
        g_op.pop(int(p_choice) - 1)
        g_op.insert(int(p_choice) - 1, dictionary[n_player][1])
    else:
        print("Please select a valid option ")
        play_player(n_player)

    print(table.table.format(g_op[0], g_op[1], g_op[2], g_op[3], g_op[4], g_op[5], g_op[6], g_op[7], g_op[8]))
    win(n_player)
    turn.pop(0)

    if game_mode == "4":
        if n_player == "1":
            play_player("2")
        else:
            play_player("1")
    else:
        play_ai(game_mode)


def play_ai(game_mode):
    print(f"    AI's Turn")

    if game_mode == "1":
        ai_choice = secrets.choice(av_options)
    elif game_mode == "2":
        ai_choice = secrets.choice(av_options)
    else:
        if play_ai_hard(turn[0], ai_mark) in av_options:
            ai_choice = play_ai_hard(turn[0], ai_mark)
        else:
            ai_choice = play_ai_hard(turn[0], p_mark)

    av_options.remove(ai_choice)
    g_op.pop(int(ai_choice) - 1)
    g_op.insert(int(ai_choice) - 1, ai_mark)

    print(table.table.format(g_op[0], g_op[1], g_op[2], g_op[3], g_op[4], g_op[5], g_op[6], g_op[7], g_op[8]))
    win("1")
    turn.pop(0)
    play_player("1")


def play_ai_hard(turn, mark):
    global ai_choice
    center = [AI_LIST[4]]
    corners = [AI_LIST[0], AI_LIST[2], AI_LIST[6], AI_LIST[8]]
    edges = [AI_LIST[1], AI_LIST[3], AI_LIST[5], AI_LIST[7]]
    if turn == "1":
        ai_choice = secrets.choice(corners + center)

        return ai_choice

    if turn == "2":
        if g_op[4] == "":
            ai_choice = AI_LIST[4]
        else:
            ai_choice = secrets.choice(corners)

        return ai_choice

    else:
        # Win Moves / Block Moves
        if (g_op[0], g_op[1]) == (mark, mark) and g_op[2] == "":
            ai_choice = AI_LIST[2]
        elif (g_op[0], g_op[4]) == (mark, mark) and g_op[8] == "":
            ai_choice = AI_LIST[8]
        elif (g_op[0], g_op[3]) == (mark, mark) and g_op[6] == "":
            ai_choice = AI_LIST[6]
        elif (g_op[1], g_op[2]) == (mark, mark) and g_op[0] == "":
            ai_choice = AI_LIST[0]
        elif (g_op[1], g_op[4]) == (mark, mark) and g_op[7] == "":
            ai_choice = AI_LIST[7]
        elif (g_op[2], g_op[4]) == (mark, mark) and g_op[6] == "":
            ai_choice = AI_LIST[6]
        elif (g_op[2], g_op[5]) == (mark, mark) and g_op[8] == "":
            ai_choice = AI_LIST[8]
        elif (g_op[3], g_op[4]) == (mark, mark) and g_op[5] == "":
            ai_choice = AI_LIST[5]
        elif (g_op[3], g_op[6]) == (mark, mark) and g_op[0] == "":
            ai_choice = AI_LIST[0]
        elif (g_op[4], g_op[5]) == (mark, mark) and g_op[3] == "":
            ai_choice = AI_LIST[3]
        elif (g_op[4], g_op[6]) == (mark, mark) and g_op[2] == "":
            ai_choice = AI_LIST[2]
        elif (g_op[4], g_op[7]) == (mark, mark) and g_op[1] == "":
            ai_choice = AI_LIST[1]
        elif (g_op[4], g_op[8]) == (mark, mark) and g_op[0] == "":
            ai_choice = AI_LIST[0]
        elif (g_op[5], g_op[8]) == (mark, mark) and g_op[2] == "":
            ai_choice = AI_LIST[2]
        elif (g_op[6], g_op[7]) == (mark, mark) and g_op[8] == "":
            ai_choice = AI_LIST[8]
        elif (g_op[7], g_op[8]) == (mark, mark) and g_op[6] == "":
            ai_choice = AI_LIST[6]

        # Win Forks / Block Forks
        elif (g_op[0], g_op[2]) == (mark, mark) and g_op[1] == "":
            ai_choice = AI_LIST[1]
        elif (g_op[0], g_op[8]) == (mark, mark) and g_op[4] == "":
            ai_choice = AI_LIST[4]
        elif (g_op[0], g_op[6]) == (mark, mark) and g_op[3] == "":
            ai_choice = AI_LIST[3]
        elif (g_op[1], g_op[7]) == (mark, mark) and g_op[4] == "":
            ai_choice = AI_LIST[4]
        elif (g_op[2], g_op[6]) == (mark, mark) and g_op[4] == "":
            ai_choice = AI_LIST[4]
        elif (g_op[2], g_op[8]) == (mark, mark) and g_op[5] == "":
            ai_choice = AI_LIST[5]
        elif (g_op[3], g_op[5]) == (mark, mark) and g_op[4] == "":
            ai_choice = AI_LIST[4]
        elif (g_op[6], g_op[8]) == (mark, mark) and g_op[7] == "":
            ai_choice = AI_LIST[7]

        # Others Win Forks / Block Forks
        elif (g_op[1], g_op[3]) == (mark, mark) and (g_op[0], g_op[2], g_op[6]) == ("", "", ""):
            ai_choice = AI_LIST[0]
        elif (g_op[1], g_op[6]) == (mark, mark) and (g_op[0], g_op[2], g_op[3]) == ("", "", ""):
            ai_choice = AI_LIST[0]
        elif (g_op[2], g_op[3]) == (mark, mark) and (g_op[0], g_op[1], g_op[6]) == ("", "", ""):
            ai_choice = AI_LIST[0]
        elif (g_op[1], g_op[5]) == (mark, mark) and (g_op[0], g_op[2], g_op[8]) == ("", "", ""):
            ai_choice = AI_LIST[2]
        elif (g_op[0], g_op[5]) == (mark, mark) and (g_op[1], g_op[2], g_op[8]) == ("", "", ""):
            ai_choice = AI_LIST[2]
        elif (g_op[1], g_op[8]) == (mark, mark) and (g_op[0], g_op[2], g_op[5]) == ("", "", ""):
            ai_choice = AI_LIST[2]
        elif (g_op[3], g_op[7]) == (mark, mark) and (g_op[0], g_op[6], g_op[8]) == ("", "", ""):
            ai_choice = AI_LIST[6]
        elif (g_op[0], g_op[7]) == (mark, mark) and (g_op[3], g_op[6], g_op[8]) == ("", "", ""):
            ai_choice = AI_LIST[6]
        elif (g_op[3], g_op[8]) == (mark, mark) and (g_op[0], g_op[6], g_op[7]) == ("", "", ""):
            ai_choice = AI_LIST[6]
        elif (g_op[5], g_op[7]) == (mark, mark) and (g_op[2], g_op[6], g_op[8]) == ("", "", ""):
            ai_choice = AI_LIST[8]
        elif (g_op[2], g_op[7]) == (mark, mark) and (g_op[5], g_op[6], g_op[8]) == ("", "", ""):
            ai_choice = AI_LIST[8]
        elif (g_op[5], g_op[6]) == (mark, mark) and (g_op[2], g_op[7], g_op[8]) == ("", "", ""):
            ai_choice = AI_LIST[8]

        elif (g_op[0], g_op[8]) == (mark, mark) and (g_op[1], g_op[2], g_op[3], g_op[5], g_op[6], g_op[7]) == ("", "", "", "", "", ""):
            ai_choice = secrets.choice(edges)
        elif (g_op[2], g_op[6]) == (mark, mark) and (g_op[0], g_op[1], g_op[3], g_op[5], g_op[7], g_op[8]) == ("", "", "", "", "", ""):
            ai_choice = secrets.choice(edges)

        # Others Moves
        elif mark == p_mark:
            # Search Forks
            if g_op[0] not in ("", mark) and (g_op[1], g_op[2]) == ("", ""):
                ai_choice = AI_LIST[2]
            elif g_op[0] not in ("", mark) and (g_op[4], g_op[8]) == ("", ""):
                ai_choice = AI_LIST[8]
            elif g_op[0] not in ("", mark) and (g_op[3], g_op[6]) == ("", ""):
                ai_choice = AI_LIST[6]
            elif g_op[1] not in ("", mark) and (g_op[4], g_op[7]) == ("", ""):
                ai_choice = AI_LIST[7]
            elif g_op[2] not in ("", mark) and (g_op[0], g_op[1]) == ("", ""):
                ai_choice = AI_LIST[0]
            elif g_op[2] not in ("", mark) and (g_op[4], g_op[6]) == ("", ""):
                ai_choice = AI_LIST[6]
            elif g_op[2] not in ("", mark) and (g_op[5], g_op[8]) == ("", ""):
                ai_choice = AI_LIST[8]
            elif g_op[3] not in ("", mark) and (g_op[4], g_op[5]) == ("", ""):
                ai_choice = AI_LIST[5]
            elif g_op[4] not in ("", mark) and (g_op[0], g_op[8]) == ("", ""):
                ai_choice = secrets.choice([AI_LIST[0], AI_LIST[8]])
            elif g_op[4] not in ("", mark) and (g_op[1], g_op[7]) == ("", ""):
                ai_choice = secrets.choice([AI_LIST[1], AI_LIST[7]])
            elif g_op[4] not in ("", mark) and (g_op[2], g_op[6]) == ("", ""):
                ai_choice = secrets.choice([AI_LIST[2], AI_LIST[6]])
            elif g_op[4] not in ("", mark) and (g_op[3], g_op[5]) == ("", ""):
                ai_choice = secrets.choice([AI_LIST[3], AI_LIST[5]])
            elif g_op[5] not in ("", mark) and (g_op[3], g_op[4]) == ("", ""):
                ai_choice = AI_LIST[3]
            elif g_op[6] not in ("", mark) and (g_op[0], g_op[3]) == ("", ""):
                ai_choice = AI_LIST[0]
            elif g_op[6] not in ("", mark) and (g_op[2], g_op[4]) == ("", ""):
                ai_choice = AI_LIST[2]
            elif g_op[6] not in ("", mark) and (g_op[7], g_op[8]) == ("", ""):
                ai_choice = AI_LIST[8]
            elif g_op[7] not in ("", mark) and (g_op[1], g_op[4]) == ("", ""):
                ai_choice = AI_LIST[1]
            elif g_op[8] not in ("", mark) and (g_op[2], g_op[5]) == ("", ""):
                ai_choice = AI_LIST[2]
            elif g_op[8] not in ("", mark) and (g_op[0], g_op[4]) == ("", ""):
                ai_choice = AI_LIST[0]
            elif g_op[8] not in ("", mark) and (g_op[6], g_op[7]) == ("", ""):
                ai_choice = AI_LIST[6]

            # Opposite Corner
            elif g_op[0] == mark and g_op[8] == "":
                ai_choice = AI_LIST[8]
            elif g_op[2] == mark and g_op[6] == "":
                ai_choice = AI_LIST[6]
            elif g_op[6] == mark and g_op[2] == "":
                ai_choice = AI_LIST[2]
            elif g_op[8] == mark and g_op[0] == "":
                ai_choice = AI_LIST[0]

            # Corner
            elif g_op[0] == "":
                ai_choice = AI_LIST[0]
            elif g_op[2] == "":
                ai_choice = AI_LIST[2]
            elif g_op[6] == "":
                ai_choice = AI_LIST[6]
            elif g_op[8] == "":
                ai_choice = AI_LIST[8]

            # Edge
            elif g_op[1] == "":
                ai_choice = AI_LIST[1]
            elif g_op[3] == "":
                ai_choice = AI_LIST[3]
            elif g_op[5] == "":
                ai_choice = AI_LIST[5]
            elif g_op[7] == "":
                ai_choice = AI_LIST[7]

        return ai_choice

def win(n_player):
    if len(av_options) <= 4:
        if g_op[0] == g_op[1] and g_op[0] == g_op[2] and (g_op[0], g_op[1], g_op[2]) != ("", "", ""):
            win_message(n_player)
            exit()
        elif g_op[0] == g_op[3] and g_op[0] == g_op[6] and (g_op[0], g_op[3], g_op[6]) != ("", "", ""):
            win_message(n_player)
            exit()
        elif g_op[0] == g_op[4] and g_op[0] == g_op[8] and (g_op[0], g_op[4], g_op[8]) != ("", "", ""):
            win_message(n_player)
            exit()
        elif g_op[1] == g_op[4] and g_op[1] == g_op[7] and (g_op[1], g_op[4], g_op[7]) != ("", "", ""):
            win_message(n_player)
            exit()
        elif g_op[2] == g_op[5] and g_op[2] == g_op[8] and (g_op[2], g_op[5], g_op[8]) != ("", "", ""):
            win_message(n_player)
            exit()
        elif g_op[2] == g_op[4] and g_op[2] == g_op[6] and (g_op[2], g_op[4], g_op[6]) != ("", "", ""):
            win_message(n_player)
            exit()
        elif g_op[3] == g_op[4] and g_op[3] == g_op[5] and (g_op[3], g_op[4], g_op[5]) != ("", "", ""):
            win_message(n_player)
            exit()
        elif g_op[6] == g_op[7] and g_op[6] == g_op[8] and (g_op[6], g_op[7], g_op[8]) != ("", "", ""):
            win_message(n_player)
            exit()

    if len(av_options) == 0:
        if g_op.count("X") == g_op.count("O") + 1:
            tie_message()
            exit()


def win_message(n_player):
    player_win = f"Congratulations {dictionary[n_player][0]}!, you won the game in {turn[0]} turns"
    ai_win = f"AI won the game in {turn[0]} turns, better luck next time pal!"

    if g_op.count("X") > g_op.count("O") and p_mark == "X":
        print(player_win)
    elif g_op.count("X") > g_op.count("O") and ai_mark == "X":
        if game_mode == "4":
            print(player_win)
        else:
            print(ai_win)
    elif g_op.count("O") == g_op.count("X") and p_mark == "O":
        print(player_win)
    elif g_op.count("O") == g_op.count("X") and ai_mark == "O":
        if game_mode == "4":
            print(player_win)
        else:
            print(ai_win)



def tie_message():
    print(" Tie! ")


if __name__ == "__main__":
    start()


