
top_left = "┌"
top_right = "┐"
bot_left = "└"
bot_right = "┘"

top_middle = "┬"
mid_center = "┼"
bot_middle = "┴"

mid_left = "├"
mid_right = "┤"

h_line = 3 * "──"
v_line = "│"

space_1 = "  1   "  # 6 spaces
space_2 = "  2   "
space_3 = "  3   "
space_4 = "  4   "
space_5 = "  5   "
space_6 = "  6   "
space_7 = "  7   "
space_8 = "  8   "
space_9 = "  9   "

row_1 = v_line + space_1 + v_line + space_2 + v_line + space_3 + v_line
row_2 = v_line + space_4 + v_line + space_5 + v_line + space_6 + v_line
row_3 = v_line + space_7 + v_line + space_8 + v_line + space_9 + v_line

example_table = " " + top_left + h_line + top_middle + h_line + top_middle + h_line + top_right + "\n"\
        " " + v_line + space_1 + v_line + space_2 + v_line + space_3 + v_line + "\n"\
        " " + mid_left + h_line + mid_center + h_line + mid_center + h_line + mid_right + "\n"\
        " " + v_line + space_4 + v_line + space_5 + v_line + space_6 + v_line + "\n"\
        " " + mid_left + h_line + mid_center + h_line + mid_center + h_line + mid_right + "\n"\
        " " + v_line + space_7 + v_line + space_8 + v_line + space_9 + v_line + "\n"\
        " " + bot_left + h_line + bot_middle + h_line + bot_middle + h_line + bot_right + "\n"\

table = " " + top_left + h_line + top_middle + h_line + top_middle + h_line + top_right + "\n"\
        " " + v_line + "  {:^2}  " + v_line + "  {:^2}  " + v_line + "  {:^2}  " + v_line + "\n"\
        " " + mid_left + h_line + mid_center + h_line + mid_center + h_line + mid_right + "\n"\
        " " + v_line + "  {:^2}  " + v_line + "  {:^2}  " + v_line + "  {:^2}  "+ v_line + "\n"\
        " " + mid_left + h_line + mid_center + h_line + mid_center + h_line + mid_right + "\n"\
        " " + v_line + "  {:^2}  " + v_line + "  {:^2}  " + v_line + "  {:^2}  " + v_line + "\n"\
        " " + bot_left + h_line + bot_middle + h_line + bot_middle + h_line + bot_right + "\n"\




