
top_left = "╔"
top_right = "╗"
bot_left = "╚"
bot_right = "╝"

top_middle = "╤"
mid_center = "┼"
bot_middle = "╧"

mid_left = "╟"
mid_right = "╢"

h_line = "──" * 3
v_line = "│"
h_line_tb = "══" * 3
v_line_tb = "║"

space_1 = "  1   "  # 6 spaces
space_2 = "  2   "
space_3 = "  3   "
space_4 = "  4   "
space_5 = "  5   "
space_6 = "  6   "
space_7 = "  7   "
space_8 = "  8   "
space_9 = "  9   "

example_board = " " + top_left + h_line_tb + top_middle + h_line_tb + top_middle + h_line_tb + top_right + "\n"\
        " " + v_line_tb + space_1 + v_line + space_2 + v_line + space_3 + v_line_tb + "\n"\
        " " + mid_left + h_line + mid_center + h_line + mid_center + h_line + mid_right + "\n"\
        " " + v_line_tb + space_4 + v_line + space_5 + v_line + space_6 + v_line_tb + "\n"\
        " " + mid_left + h_line + mid_center + h_line + mid_center + h_line + mid_right + "\n"\
        " " + v_line_tb + space_7 + v_line + space_8 + v_line + space_9 + v_line_tb + "\n"\
        " " + bot_left + h_line_tb + bot_middle + h_line_tb + bot_middle + h_line_tb + bot_right + "\n"\

board = " " + top_left + h_line_tb + top_middle + h_line_tb + top_middle + h_line_tb + top_right + "\n"\
        " " + v_line_tb + "  {:^2}  " + v_line + "  {:^2}  " + v_line + "  {:^2}  " + v_line_tb + "\n"\
        " " + mid_left + h_line + mid_center + h_line + mid_center + h_line + mid_right + "\n"\
        " " + v_line_tb + "  {:^2}  " + v_line + "  {:^2}  " + v_line + "  {:^2}  " + v_line_tb + "\n"\
        " " + mid_left + h_line + mid_center + h_line + mid_center + h_line + mid_right + "\n"\
        " " + v_line_tb + "  {:^2}  " + v_line + "  {:^2}  " + v_line + "  {:^2}  " + v_line_tb + "\n"\
        " " + bot_left + h_line_tb + bot_middle + h_line_tb + bot_middle + h_line_tb + bot_right + "\n"\

