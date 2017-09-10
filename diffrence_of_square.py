#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

def square_of_sum(num):
    the_list = range(num+1)
    return pow(sum(the_list), 2)

def sum_of_square(num):
    the_list = [ pow(x, 2) for x in range(num+1) ]

    return sum(the_list)

def diff(num):
    return square_of_sum(num) - sum_of_square(num)

def main():
    print diff(2)

if __name__ == '__main__':
    main()
