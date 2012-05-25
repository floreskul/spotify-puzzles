"""
Solution to the 'Best Before' Spotify puzzle:
http://www.spotify.com/int/jobs/tech/best-before/
"""

__author__ = "Volodymyr Floreskul"
__email__ = "volodymyr@floreskul.name"
__date__ = "2012-04-22"

import datetime
import itertools


def get_earliest_date(numbers):
    '''Get earliest valid date from the combination of 3 numbers.'''

    if len(numbers) != 3:
        return None

    earliest_date = datetime.date.max
    for permutation in itertools.permutations(numbers):
        year, month, day = permutation
        # assume that all xx years correspond to the year 20xx
        if year < 100:
            year += 2000
        try:
            possible_date = datetime.date(year, month, day)
            earliest_date = min(earliest_date, possible_date)
        except ValueError:
            pass

    if earliest_date == datetime.date.max:
        return None
    return earliest_date


if __name__ == '__main__':
    line = raw_input()
    numbers = map(int, line.split('/'))
    earliest_date = get_earliest_date(numbers)
    if earliest_date:
        print earliest_date.isoformat()
    else:
        print "{} is illegal".format(line)
