#!/usr/bin/python
# n = num of plays per round
# 1 play = [r], [p], [s]
# 2 play = [r,r], [r,p], [r,s], [p,r], [p,p], [p,s], [s,r], [s,p], [s,s]
# plays = [0] * n
# set up helper to "trigger" rps
# needs an array, an index, and result
# set the index to equal the array length
# append array to the result
# look at the item of ("rock", "paper", "scissors")
# set the index of the array to this item
# apply the "trigger"
# set n to 0 and return empyt []
# set result to empty []
# set num of plays to [0] * n
# call helper before returning the result


import sys


def rock_paper_scissors(n):
    if n == 0:
        return [[]]

    result = []
    num_of_plays = [0]*n  # n is the number of plays
    trigger_rps(num_of_plays, 0, result)
    return result


def trigger_rps(arr, index, result):

    if index == len(arr):
        result.append(list(arr))
        return arr

    for item in ("rock", "paper", "scissors"):
        arr[index] = item
        trigger_rps(arr, index+1, result)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
