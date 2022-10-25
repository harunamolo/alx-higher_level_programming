#!/usr/bin/python3
"""pascal_triangle
"""


def pascal_triangle(n):
    """ends of each list in the matrix are summed to display the next list
    until the middle of the list. The number '1' is always at both ends.
    """
    if n <= 0:
        return []

    res = []
    for elem in range(n):
        if elem == 0:
            res.append([1])
            continue
        if elem == 1:
            res.append([1, 1])
            continue
        row = []
        # init row
        for item in range(elem + 1):
            row.append(item)
        for item in range(1, elem):
            row[0] = 1
            row[elem] = 1
            row[item] = res[elem - 1][item] + res[elem - 1][item - 1]
        res.append(row)
            
    return res
