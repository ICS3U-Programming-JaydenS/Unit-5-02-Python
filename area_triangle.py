#!/usr/bin/env python3
# Created By: Jayden Smith
# Date: May 7, 2025
# This code calculates the area of a triangle


def area_triangle(base, height):

    # Calculates and prints area
    area = (base * height) / 2
    print("The area of the triangle is ", area, "cm^2")


def main():
    # Get user input
    user_base = input("What is your base of your triangle (cm) ? ")
    user_height = input("What is the height of your triangle (cm) ? ")
    # Convert the two inputs in nested try catch to float
    try:
        base_float = float(user_base)
        try:
            height_float = float(user_height)

            # If they are negative this happens
            if height_float < 0:
                print(height_float, "is not a positive float!")
            elif base_float < 0:
                print(base_float, "is not a positive float!")

            # If not the function is called
            else:
                area_triangle(base_float, height_float)
        # Try catch for user height
        except Exception:
            print(user_height, "is not a float")

    # Try catch for user base
    except Exception:
        print(user_base, "is not a float")


if __name__ == "__main__":
    main()
