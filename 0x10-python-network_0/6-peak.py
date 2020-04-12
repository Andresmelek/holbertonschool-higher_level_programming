#!/usr/bin/python3
""" Find poeak in unsorted array """


def find_peak(list_of_integers):
    """function that finds peak"""
    if not list_of_integers:
        return None

    lenght = len(list_of_integers)
    if (lenght == 1):
        return list_of_integers[0]

    if (lenght == 2):
        if (list_of_integers[0] > list_of_integers[1]):
            return list_of_integers[0]
        else:
            return list_of_integers[1]

    half = int((lenght - 1) / 2)
    if (list_of_integers[half] < list_of_integers[half + 1]):
        return find_peak(list_of_integers[half + 1:])
    else:
        return find_peak(list_of_integers[:half + 1])
