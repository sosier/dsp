"""
The football.csv file contains the results from the English Premier League.
The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of
goals scored for and against each team in that season (so Arsenal scored 79
goals against opponents, and had 36 goals scored against them). Write a program
to read the file, then print the name of the team with the smallest difference
in ‘for’ and ‘against’ goals.
"""

import csv


def read_data(data):
    parsed = []

    f = open(data, "r")
    try:
        reader = csv.reader(f)
        for row in reader:
            parsed.append(row)
    finally:
        f.close()

    return parsed


def get_min_score_difference(parsed_data):
    headers = parsed_data[0]
    goals_i = headers.index("Goals")
    allowed_i = headers.index("Goals Allowed")

    scoreDiffs = [abs(int(x[goals_i]) - int(x[allowed_i]))
                  for x in parsed_data[1:]]  # Header row not included
    """
    Note assumes that by "smallest difference in ‘for’ and ‘against’ goals"
    we want the minimum absolute difference (NOT the most negative difference)
    """

    minimum = min(scoreDiffs)
    min_i = scoreDiffs.index(minimum) + 1  # Add 1 to account for header row

    return min_i


def get_team(index_value, parsed_data):
    headers = parsed_data[0]
    team_i = headers.index("Team")

    return parsed_data[index_value][team_i]


data = read_data("python/football.csv")
min_i = get_min_score_difference(data)
result = get_team(min_i, data)
print(result)  # Prints "Aston_Villa"
"""
Again, this assumes that by "smallest difference in ‘for’ and ‘against’ goals"
we want the minimum absolute difference (NOT the most negative difference)
"""
