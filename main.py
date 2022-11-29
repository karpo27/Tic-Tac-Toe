# Scripts:
from table import *
from score_db import *
from constants import *

# Modules:
import secrets
import time

av_options = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
g_op = ["", "", "", "", "", "", "", "", ""]
turn = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
ai_choice = ""


def start():
    create_table()

    print("\n"
          "Welcome to Tic Tac Toe game!\n"
          "")
    rules = input("If you already know the rules press any key to continue, otherwise type 'help'. ")

    if rules in ['help', 'HELP', 'Help']:
        print("\n"
              "1. The game is played on a grid that's 3 squares by 3 squares.\n"
              "2. You can choose 'X' or 'O' and the other person or AI uses the remaining option.\n"
              "3. Players take turns putting their marks in empty squares. Squares are identified with numbers:\n"
              f"{example_table}"
              "4. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.\n"
              "5. When all 9 squares are full, the game is over. "
              "If no player has 3 marks in a row, the game ends in a tie.")

    select_name("1")


def select_name(n_player):
    if n_player == "1":
        global name_p1
        name_p1 = input("\n"
                        "Player 1 please enter your name: ")
        if name_p1 == "":
            name_p1 = "Mysterious Guy"
        else:
            insert_player_name(name_p1)

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
        else:
            insert_player_name(name_p2)

        print(f"\n"
              f"Hello {name_p2}!")

        dictionary.update({"2": name_p2})
        select_mark()


def select_game_mode():
    global game_mode
    game_mode = input("\n"
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
                   f"{name_p1} choose 'X' or 'O' (remember 'X' moves first)\n"
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
              f"  »  {dictionary[n_player][0]}'s Turn")
        print(table.format(g_op[0], g_op[1], g_op[2], g_op[3], g_op[4], g_op[5], g_op[6], g_op[7], g_op[8]))
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

    time.sleep(0.4)
    print(table.format(g_op[0], g_op[1], g_op[2], g_op[3], g_op[4], g_op[5], g_op[6], g_op[7], g_op[8]))
    check_win(n_player)
    turn.pop(0)

    if game_mode == "4":
        if n_player == "1":
            play_player("2")
        else:
            play_player("1")
    else:
        play_ai(game_mode)


def play_ai(game_mode):
    print("  »  AI's Turn")

    if game_mode == "1":  # 65% AI Hard
        ai_choice = secrets.choice(set_conditional_choice(65, play_ai_hard(turn[0])))
    elif game_mode == "2":  # 88% AI Hard
        ai_choice = secrets.choice(set_conditional_choice(88, play_ai_hard(turn[0])))
    else:  # AI Hard
        ai_choice = play_ai_hard(turn[0])

    av_options.remove(ai_choice)
    g_op.pop(int(ai_choice) - 1)
    g_op.insert(int(ai_choice) - 1, ai_mark)

    time.sleep(0.4)
    print(table.format(g_op[0], g_op[1], g_op[2], g_op[3], g_op[4], g_op[5], g_op[6], g_op[7], g_op[8]))
    check_win("1")
    turn.pop(0)
    play_player("1")


def set_conditional_choice(probability, ai_hard_choice):
    prob_list = []
    while probability > (prob_list + av_options).count(ai_hard_choice) * 100 / len(prob_list + av_options):
        prob_list.append(ai_hard_choice)

    return av_options + prob_list


def play_ai_hard(n_turn):
    if n_turn == "1":
        return secrets.choice(CORNERS + CENTER)

    if n_turn == "2":
        if g_op[4] == "":
            return AI_LIST[4]
        else:
            return secrets.choice(CORNERS)

    else:
        choice_list = [check_win_or_block(ai_mark), check_win_or_block(p_mark), check_forks(ai_mark),
                       check_forks(p_mark), check_other_moves(ai_mark), check_other_moves(p_mark),
                       check_final_moves(ai_mark), check_final_moves(p_mark)]

        for i in choice_list:
            if i in av_options:
                return i


def check_win_or_block(mark):
    # Win Moves, Forks / Block Moves, Forks
    r1 = [g_op[0], g_op[1], g_op[2]]
    r2 = [g_op[3], g_op[4], g_op[5]]
    r3 = [g_op[6], g_op[7], g_op[8]]
    c1 = [g_op[0], g_op[3], g_op[6]]
    c2 = [g_op[1], g_op[4], g_op[7]]
    c3 = [g_op[2], g_op[5], g_op[8]]
    d1 = [g_op[0], g_op[4], g_op[8]]
    d2 = [g_op[2], g_op[4], g_op[6]]
    all_op = [r1, r2, r3, c1, c2, c3, d1, d2]

    for i in range(len(all_op)):
        if (all_op[i][0], all_op[i][1]) == (mark, mark) and all_op[i][2] == "":
            return ALL_OP[i][2]
        elif (all_op[i][0], all_op[i][2]) == (mark, mark) and all_op[i][1] == "":
            return ALL_OP[i][1]
        elif (all_op[i][1], all_op[i][2]) == (mark, mark) and all_op[i][0] == "":
            return ALL_OP[i][0]


def check_forks(mark):
    # Others Win Forks / Block Forks
    if (g_op[1], g_op[3]) == (mark, mark) and (g_op[0], g_op[2], g_op[6]) == ("", "", ""):
        return AI_LIST[0]
    elif (g_op[1], g_op[6]) == (mark, mark) and (g_op[0], g_op[2], g_op[3]) == ("", "", ""):
        return AI_LIST[0]
    elif (g_op[2], g_op[3]) == (mark, mark) and (g_op[0], g_op[1], g_op[6]) == ("", "", ""):
        return AI_LIST[0]
    elif (g_op[1], g_op[5]) == (mark, mark) and (g_op[0], g_op[2], g_op[8]) == ("", "", ""):
        return AI_LIST[2]
    elif (g_op[0], g_op[5]) == (mark, mark) and (g_op[1], g_op[2], g_op[8]) == ("", "", ""):
        return AI_LIST[2]
    elif (g_op[1], g_op[8]) == (mark, mark) and (g_op[0], g_op[2], g_op[5]) == ("", "", ""):
        return AI_LIST[2]
    elif (g_op[3], g_op[7]) == (mark, mark) and (g_op[0], g_op[6], g_op[8]) == ("", "", ""):
        return AI_LIST[6]
    elif (g_op[0], g_op[7]) == (mark, mark) and (g_op[3], g_op[6], g_op[8]) == ("", "", ""):
        return AI_LIST[6]
    elif (g_op[3], g_op[8]) == (mark, mark) and (g_op[0], g_op[6], g_op[7]) == ("", "", ""):
        return AI_LIST[6]
    elif (g_op[5], g_op[7]) == (mark, mark) and (g_op[2], g_op[6], g_op[8]) == ("", "", ""):
        return AI_LIST[8]
    elif (g_op[2], g_op[7]) == (mark, mark) and (g_op[5], g_op[6], g_op[8]) == ("", "", ""):
        return AI_LIST[8]
    elif (g_op[5], g_op[6]) == (mark, mark) and (g_op[2], g_op[7], g_op[8]) == ("", "", ""):
        return AI_LIST[8]

    elif (g_op[0], g_op[8]) == (mark, mark) and (g_op[1], g_op[2], g_op[3], g_op[5], g_op[6], g_op[7]) == ("", "", "", "", "", ""):
        return secrets.choice(EDGES)
    elif (g_op[2], g_op[6]) == (mark, mark) and (g_op[0], g_op[1], g_op[3], g_op[5], g_op[7], g_op[8]) == ("", "", "", "", "", ""):
        return secrets.choice(EDGES)


def check_other_moves(mark):
    # Search Forks or Win Condition
    if g_op[0] not in ("", mark):
        if (g_op[1], g_op[2]) == ("", ""):
            return AI_LIST[2]
        elif (g_op[4], g_op[8]) == ("", ""):
            return AI_LIST[4]
        elif (g_op[3], g_op[6]) == ("", ""):
            return AI_LIST[6]

    elif g_op[1] not in ("", mark) and (g_op[4], g_op[7]) == ("", ""):
        return AI_LIST[7]

    elif g_op[2] not in ("", mark):
        if (g_op[0], g_op[1]) == ("", ""):
            return AI_LIST[0]
        elif (g_op[4], g_op[6]) == ("", ""):
            return AI_LIST[4]
        elif (g_op[5], g_op[8]) == ("", ""):
            return AI_LIST[8]

    elif g_op[3] not in ("", mark) and (g_op[4], g_op[5]) == ("", ""):
        return AI_LIST[5]

    elif g_op[5] not in ("", mark) and (g_op[3], g_op[4]) == ("", ""):
        return AI_LIST[3]

    elif g_op[6] not in ("", mark):
        if (g_op[0], g_op[3]) == ("", ""):
            return AI_LIST[0]
        elif (g_op[2], g_op[4]) == ("", ""):
            return AI_LIST[4]
        elif (g_op[7], g_op[8]) == ("", ""):
            return AI_LIST[8]

    elif g_op[7] not in ("", mark) and (g_op[1], g_op[4]) == ("", ""):
        return AI_LIST[1]

    elif g_op[8] not in ("", mark):
        if (g_op[2], g_op[5]) == ("", ""):
            return AI_LIST[2]
        elif (g_op[0], g_op[4]) == ("", ""):
            return AI_LIST[4]
        elif (g_op[6], g_op[7]) == ("", ""):
            return AI_LIST[6]

    elif g_op[4] not in ("", mark) and (g_op[0], g_op[8]) == ("", ""):
        return secrets.choice([AI_LIST[0], AI_LIST[8]])
    elif g_op[4] not in ("", mark) and (g_op[1], g_op[7]) == ("", ""):
        return secrets.choice([AI_LIST[1], AI_LIST[7]])
    elif g_op[4] not in ("", mark) and (g_op[2], g_op[6]) == ("", ""):
        return secrets.choice([AI_LIST[2], AI_LIST[6]])
    elif g_op[4] not in ("", mark) and (g_op[3], g_op[5]) == ("", ""):
        return secrets.choice([AI_LIST[3], AI_LIST[5]])


def check_final_moves(mark):
    corners = [g_op[0], g_op[2], g_op[6], g_op[8]]
    edges = [g_op[1], g_op[3], g_op[5], g_op[7]]
    # Last Empty Slots
    if (g_op[1], g_op[7]) == ("", "") and g_op[4] == mark:
        return secrets.choice([AI_LIST[1], AI_LIST[7]])
    elif (g_op[3], g_op[5]) == ("", "") and g_op[4] == mark:
        return secrets.choice([AI_LIST[3], AI_LIST[5]])
    else:
        # Opposite Corner
        for i in range(len(corners)):
            if corners[i] not in ("", mark) and list(reversed(corners))[i] == "":
                return list(reversed(CORNERS))[i]
        # Corner
        for i in range(len(corners)):
            if corners[i] == "":
                return CORNERS[i]
        # Edge
        for i in range(len(edges)):
            if edges[i] == "":
                return EDGES[i]


def check_win(n_player):
    r1 = [g_op[0], g_op[1], g_op[2]]
    r2 = [g_op[3], g_op[4], g_op[5]]
    r3 = [g_op[6], g_op[7], g_op[8]]
    c1 = [g_op[0], g_op[3], g_op[6]]
    c2 = [g_op[1], g_op[4], g_op[7]]
    c3 = [g_op[2], g_op[5], g_op[8]]
    d1 = [g_op[0], g_op[4], g_op[8]]
    d2 = [g_op[2], g_op[4], g_op[6]]
    all_op = [r1, r2, r3, c1, c2, c3, d1, d2]

    if len(av_options) <= 4:
        for i in all_op:
            if i[0] == i[1] and i[0] == i[2] and (i[0], i[1], i[2]) != ("", "", ""):
                win_message(n_player)

    if len(av_options) == 0:
        tie_message()


def win_message(n_player):
    player_win = f"Congratulations {dictionary[n_player][0]}!, you won the game in {turn[0]} turns"
    ai_win = f"AI won the game in {turn[0]} turns, better luck next time pal!"

    if g_op.count("X") > g_op.count("O") and p_mark == "X":
        print(player_win)
        if game_mode == "4":
            update_player_score(dictionary["1"][0], game_mode, 0)
            update_player_score(dictionary["2"][0], game_mode, 1)
        else:
            update_player_score(dictionary["1"][0], game_mode, 0)
    elif g_op.count("X") > g_op.count("O") and ai_mark == "X":
        if game_mode == "4":
            print(player_win)
            update_player_score(dictionary["1"][0], game_mode, 1)
            update_player_score(dictionary["2"][0], game_mode, 0)
        else:
            print(ai_win)
            update_player_score(dictionary[n_player][0], game_mode, 1)
    elif g_op.count("O") == g_op.count("X") and p_mark == "O":
        print(player_win)
        if game_mode == "4":
            update_player_score(dictionary["1"][0], game_mode, 0)
            update_player_score(dictionary["2"][0], game_mode, 1)
        else:
            update_player_score(dictionary["1"][0], game_mode, 0)
    elif g_op.count("O") == g_op.count("X") and ai_mark == "O":
        if game_mode == "4":
            print(player_win)
            update_player_score(dictionary["2"][0], game_mode, 0)
            update_player_score(dictionary["1"][0], game_mode, 1)
        else:
            print(ai_win)
            update_player_score(dictionary[n_player][0], game_mode, 1)

    play_again()


def tie_message():
    print(" Tie! ")
    if game_mode == "4":
        update_player_score(dictionary["1"][0], game_mode, 2)
        update_player_score(dictionary["2"][0], game_mode, 2)
    else:
        update_player_score(dictionary["1"][0], game_mode, 2)

    play_again()


def play_again():
    av_options.clear()
    g_op.clear()
    turn.clear()

    av_options.extend(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
    g_op.extend(["", "", "", "", "", "", "", "", ""])
    turn.extend(["1", "2", "3", "4", "5", "6", "7", "8", "9"])

    final_choice = input("\n"
                         "Do you want yo play again?\n"
                         "1- Yes, same game mode\n"
                         "2- Yes, but change game mode\n"
                         "3- No, thanks!\n"
                         "4- Show my score\n"
                         "")

    if final_choice == "4":
        if game_mode == "4":
            if name_p1 != "Mysterious Guy" and name_p2 != "Mysterious Guy's partner":
                show_data(name_p1)
                show_data(name_p2)
                play_again()
            elif name_p1 == "Mysterious Guy" and name_p2 == "Mysterious Guy's partner":
                print("\n"
                      "If you are playing nameless, you have no stats! ")
                play_again()
            elif name_p1 != "Mysterious Guy" and name_p2 == "Mysterious Guy's partner":
                show_data(name_p1)
                play_again()
            elif name_p1 == "Mysterious Guy" and name_p2 != "Mysterious Guy's partner":
                show_data(name_p2)
                play_again()
        else:
            if name_p1 != "Mysterious Guy":
                show_data(name_p1)
                play_again()
            elif name_p1 == "Mysterious Guy":
                print("\n"
                      "If you are playing nameless, you have no stats! ")
                play_again()
    elif final_choice == "1":
        select_mark()
    elif final_choice == "2":
        select_game_mode()
    elif final_choice == "3":
        exit()
    else:
        print("\n"
              "Please select a valid option ")
        play_again()


if __name__ == "__main__":
    start()
