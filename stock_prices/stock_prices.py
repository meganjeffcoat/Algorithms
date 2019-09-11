#!/usr/bin/python

# TODO:
# set current_min_price_so_far to 0
# set max_profit_so_far to 0
# need to go throug prices to retreive max_profit_so_far and get max_price_so_far
# need to get todays profit by max_price_so_far - current_min_price_so_far
# compare todays profit with  todays max profit
# todays max profit = todays profit
# compare prices with current_min_price_so_far
# return max_profit_so_far

import argparse


def find_max_profit(prices):
    current_min_price_so_far = prices[0]  # set current_min_price_so_far to 0
    max_profit_so_far = 0  # set max_profit_so_far to 0
    for i in range(1, len(prices) - 1):
        if prices[i] > current_min_price_so_far:
            max_price_so_far = prices[i]
            today_profit = max_price_so_far - current_min_price_so_far
            if today_profit > max_profit_so_far:
                max_profit_so_far = today_profit

        if prices[i] < current_min_price_so_far:
            current_min_price_so_far = prices[i]
    return max_profit_so_far


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
