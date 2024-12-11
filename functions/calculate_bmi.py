#!/usr/bin/env python3
"""
BMI Calculator Application

This application calculates the Body Mass Index (BMI)
based on user input for weight and height.

Features:
    - Command-line usage for quick calculations.
    - Interactive mode with unit conversion support.
    - Categorizes BMI based on health standards.

Usage:
    From the command line:
        ./calculate_bmi.py <weight_in_kg> <height_in_meters>
        Example:
            ./calculate_bmi.py 80 1.8

    Interactive mode:
        Simply run the script without arguments to enter interactive mode.

BMI Categories:
    - Underweight: BMI < 18.5
    - Normal weight: 18.5 <= BMI < 24.9
    - Overweight: 25 <= BMI < 29.9
    - Obesity: BMI >= 30
"""
import sys


def calculate_bmi(weight: float, height: float) -> float:
    """
    Calculate the Body Mass Index (BMI).

    Args:
        weight (float): Weight in kilograms (must be > 0).
        height (float): Height in meters (must be > 0).

    Returns:
        float: The calculated BMI.

    Raises:
        ValueError: If weight or height is less than or equal to zero.
    """
    if height <= 0:
        raise ValueError("Height must be greater than zero")
    if weight <= 0:
        raise ValueError("Weight must be greater than zero")

    bmi = weight / (height ** 2)
    return bmi


def bmi_category(bmi: float) -> str:
    """
    Determine the BMI category based on the BMI value.

    Args:
        bmi (float): The BMI value.

    Returns:
        str: The BMI category.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"


def interactive_mode():
    """Run the application in interactive mode."""
    print("Welcome to the BMI Calculator!")
    try:
        weight_unit = input("Enter your weight unit (kg or lbs): ").strip()\
            .lower()
        weight = float(input("Enter your weight: "))
        if weight_unit == "lbs":
            weight = weight * 0.453592  # Convert pounds to kilograms

        height_unit = input("Enter your height unit (m or inches): ")\
            .strip().lower()
        height = float(input("Enter your height: "))
        if height_unit == "inches":
            height = height * 0.0254  # Convert inches to meters

        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)

        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"BMI Category: {category}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    # Command-line arguments mode
    if len(sys.argv) == 3:
        try:
            weight = float(sys.argv[1])
            height = float(sys.argv[2])

            bmi = calculate_bmi(weight, height)
            category = bmi_category(bmi)

            print(f"The calculated BMI is: {bmi:.2f}")
            print(f"BMI Category: {category}")
        except ValueError as e:
            print(f"Error: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"Unexpected error: {e}")
            sys.exit(1)
    else:
        # Interactive mode
        interactive_mode()
