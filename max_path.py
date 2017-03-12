#!/usr/bin/python2.7
# vim:fileencoding=utf8
# -*- coding: utf-8 -*-

"""
    consider the problem as a sub problem:  (M-1*N or M*N-1 step) + last step
"""

def max_path_finder(the_map, actual_x=None, actual_y=None):
    if actual_x == None:
        actual_x = len(the_map) - 1
    if actual_y == None:
        actual_y = len(the_map[0]) - 1

    if actual_x == 0 and actual_y == 0:
        return the_map[0][0], [(0, 0)]

    if actual_x-1 >= 0:
        left_max, left_path = max_path_finder(the_map, actual_x-1, actual_y)
    else:
        left_max = 0

    if actual_y-1 >= 0:
        top_max, top_path = max_path_finder(the_map, actual_x, actual_y-1)
    else:
        top_max = 0

    if top_max >= left_max or actual_x-1 < 0:
        return_path = top_path
        return_max = top_max + the_map[actual_x][actual_y]
        return_path.append((actual_x, actual_y))

    elif top_max < left_max or actual_y-1 < 0:
        return_path = left_path
        return_max = left_max + the_map[actual_x][actual_y]
        return_path.append((actual_x, actual_y))

    return return_max, return_path


def main():
    print max_path_finder([[1, 0, 5], [1, 0, 0], [1, 10, 1], [1, 0, 1], [1, 0, 0]])


if __name__ == '__main__':
    main()
