#!/usr/bin/env python3
"""
Distance Converter

This script contains a function to convert distances
between kilometers and miles.

Functions:
    convert_distance(distance: float, unit: str = "km") -> float
        Converts the distance from kilometers to miles or vice versa.

Arguments:
    distance (float): The distance value to be converted.
    unit (str): The unit of the distance. Defaults to "km".
        - If unit is "km", the function converts the distance to miles.
        - If unit is "miles", the function converts the distance to kilometers.

Returns:
    float: The converted distance value.

Usage:
    From terminal (bash):
        ./convert_distance <distance> <unit>

    Example:
        ./convert_distance 5 km  # Converts 5 kilometers to miles
        ./convert_distance 3 miles  # Converts 3 miles to kilometers

    Import into a script:
        from convert_distance import convert_distance

        Example:
            km_to_miles = convert_distance(5, "km")
            miles_to_km = convert_distance(3, "miles")

"""

from typing import Union
from sys import argv


def convert_distance(distance:  Union[float, int], unit: str = "km") -> float:
    """
    A function that converts distances from kilometer
    to miles and vice versa
        Args:
        distance (float)
        unit (str) - unit of the distance default to "km"
        if the unit is "km", it should convert the
          distance to miles,
        and if the unit is "miles", it should convert
        the distance to kilometers.
    """
    if unit == "km":
        return distance * 0.621371
    elif unit == "miles":
        return distance / 0.621371
    else:
        raise ValueError("Invalid unit. Please use 'km' or 'miles'.")


if __name__ == "__main__":
    if len(argv) != 3:
        print("Usage: ./convert_distance <distance> <unit>")
        exit(1)
    try:
        distance = float(argv[1])
        unit = argv[2].lower()
        if unit == 'km':
            display_unit = 'miles'
        elif unit == 'miles':
            display_unit = 'km'
        print("Converted distance: {} {}".format(
            convert_distance(distance, unit),
            display_unit
        ))
    except ValueError as e:
        print(f"Error: {e}")
        exit(1)
