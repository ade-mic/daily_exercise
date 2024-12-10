#!/usr/bin/env python3
"""
This script calculates the sum of latitude and longitude
values from a variable number of coordinate pairs (tuples).
It can be used as a standalone executable or as an imported module.

Metadata
Shebang: #!/usr/bin/env python3
Filename: sum_coordinates.py
Purpose: To compute the sum of latitude and longitude
values provided as coordinate pairs.
Dependencies: None (uses Python's standard library).
Features
Accepts a variable number of coordinate pairs via
function calls or interactive terminal input.
Computes the total sums of latitude and longitude values.
Provides interactive input when executed directly.
Includes error handling for malformed input.
Usage
1. As a Script
When executed directly (__name__ == "__main__"),
    ./sum_coordinates.py "[<coordinate-pair-1>, <coordinate-pair-2>, ...]"
    ./sum_coordinates.py "[(2.5, 19.5), (6.0, 78.4), (10.1, 15.6)]"

2. As a Module
The sum_coordinates function can be imported
 and used in other Python scripts for programmatic 
 summation of coordinates.
"""
from typing import Tuple
from sys import argv
import ast

def sum_coordinates(*coordinates: Tuple[float, float]) -> Tuple:
    """
    Accepts a variable number of coordinate pairs and
      returns the sum of all latitude and longitude values.

    Parameters:
        *coordinates (tuple): A variable number of tuples, each representing a coordinate pair. 
                              Each tuple should contain two numerical values (latitude, longitude).

    Returns:
        tuple: A tuple containing two values:
               - The total sum of latitude values.
               - The total sum of longitude values.
    
    Raises:
        ValueError: If any coordinate is not a tuple of two numerical values.
        TypeError: If non-numerical values are passed as part of the coordinate tuples.

    Examples:
        >>> sum_coordinates((10, 20), (30, 40), (5, 15))
        (45, 75)

        >>> sum_coordinates((1.5, 2.5), (3.5, 4.5))
        (5.0, 7.0)

    Notes:
        - The function assumes all inputs are properly formatted and valid unless exceptions are raised.
        - If no coordinates are provided, the function returns (0, 0).
    """
    if not coordinates:
        raise ValueError("Invalid input: input the variables of turples")
    if not isinstance(coordinates, tuple):
        raise TypeError("Invalid type: Arguement must be tuple")
    total_lat = 0
    total_long = 0

    for lat, long in coordinates:
        if not ((isinstance(lat, float)) and (isinstance(long, float))):
            raise TypeError("Latitude and longitude must be numerical values.")
        total_lat += lat
        total_long += long
    return (total_lat, total_long)


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: ./sum_coordinates.py \"[<coordinate-pair-1>, <coordinate-pair-2>, ...]\"")
        exit(1)
    try:
        # Parse the input argument as a list of tuples
        coordinates = ast.literal_eval(argv[1])
        if not isinstance(coordinates, list) or not all(isinstance(coord, tuple) for coord in coordinates):
            raise ValueError("Input must be a list of tuples.")
        result = sum_coordinates(*coordinates)
        print(f"Sum of coordinates: {result}")
    except Exception as e:
        print(f"Error: {e}")
        exit(1)
