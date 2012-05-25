"""
Solution to the 'Ticket Lottery' Spotify puzzle:
http://www.spotify.com/int/jobs/tech/ticket-lottery/
"""

__author__ = "Volodymyr Floreskul"
__email__ = "volodymyr@floreskul.name"
__date__ = "2012-04-22"

import math


def binomial_coefficient(n, k):
    '''Optimized implementation of the binomial coefficient.'''

    if k < 0 or k > n:
        return 0

    # use binomial coefficient symmetry
    k = min(k, n - k)

    result = 1.0
    for i in xrange(1, k + 1):
        result *= float(n - k + i) / i
    return result


def get_probability_of_getting_tickets(m, n, t, p):
    '''Calculate the probability of getting tickets according to the task
        by using hypergeometric distribution formula.
    '''
    # we need to buy p tickets and one person can win only t of them
    number_of_needed_wins = int(math.ceil(float(p) / t))

    # calculate the probability of the opposite event
    # we lose when there are less tickets drawn then needed
    number_of_loses = 0
    for i in xrange(number_of_needed_wins):
        number_of_loses += (binomial_coefficient(m - p, n - i) *
            binomial_coefficient(p, i))

    number_of_tickets = binomial_coefficient(m, n)
    return 1 - float(number_of_loses) / number_of_tickets


if __name__ == '__main__':
    line = raw_input()
    m, n, t, p = map(int, line.split())
    print '{:.10}'.format(get_probability_of_getting_tickets(m, n, t, p))
