def calculate_area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle.

    Parameters:
    - length (float): The length of the rectangle.
    - width (float): The width of the rectangle.

    Returns:
    float: The area of the rectangle, calculated as the product of its length and width.
    """
    return length * width

def calculate_perimeter(length: float, width: float) -> float:
    """
    Calculate the perimeter of a rectangle.

    Parameters:
    - length (float): The length of the rectangle.
    - width (float): The width of the rectangle.

    Returns:
    float: The perimeter of the rectangle, calculated as 2 times the sum of its length and width.
    """
    return 2 * (length + width)

def main():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    area = calculate_area(length, width)
    perimeter = calculate_perimeter(length, width)

    print(f"Area of the rectangle: {area}")
    print(f"Perimeter of the rectangle: {perimeter}")

if __name__ == "__main__":
    main()
