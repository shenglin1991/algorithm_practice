#!/usr/bin/python2.7
# vim:fileencoding=utf8
# -*- coding: utf-8 -*-

def cut_pattern(pattern):
    result = []
    p = 0
    while p <len(pattern):
        if p + 1 < len(pattern):
            if pattern[p + 1] == '?' or pattern[p + 1] == '*':
                result.append(pattern[p: p+2])
                p = p + 2
            else:
                result.append(pattern[p])
                p = p + 1
        else:
            result.append(pattern[p])
            p = p + 1
    return result


def regex_matcher(patterns, string):
    if len(patterns) == 1:
        if len(patterns[0]) == 1:
            if patterns[0][0] == '.':
                return len(string) != 0
            else:
                if len(string) == 0:
                    return False
                return string[0] == patterns[0][0]
        else:
            return True

    if len(patterns[0]) == 1:
        if patterns[0][0] == '.':
            return len(string) != 0 and regex_matcher(patterns[1:], string[1:])
        else:
            if len(string) == 0:
                return False
            return string[0] == patterns[0][0] and regex_matcher(patterns[1:], string[1:])
    else:
        """
        pattern with * or ?
        """
        if regex_matcher(patterns[1:], string):
            return True
        if patterns[0][0] == '.':
            """
            pattern that is .? or .*
            """
            if patterns[0][1] == '?':
                return regex_matcher(patterns[1:], string[1:])
            else:
                for i in xrange(len(string)):
                    if regex_matcher(patterns[1:], string[i+1:]):
                        return True
                return False
        else:
            """
            pattern that is not .? or .*
            """
            if len(string) == 0:
                return False
            if patterns[0][1] == '?':
                return string[0] == patterns[0][0] and regex_matcher(patterns[1:], string[1:])
            else:
                for i in xrange(len(string)):
                    if string[i] != patterns[0][0]:
                        return False
                    if regex_matcher(patterns[1:], string[i+1:]):
                        return True
                return False


def simple_regex_matcher(pattern, string):
    patterns = cut_pattern(pattern)
    for i in xrange(len(string)):
        if regex_matcher(patterns, string[i:]):
            return True
    return False


def main():
    print simple_regex_matcher('x*xxxxx', 'xxxxxy')


if __name__ == '__main__':
    main()
