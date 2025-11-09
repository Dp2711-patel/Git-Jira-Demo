def multiply(a, b):
    """
    Multiply two numbers and return the product.
    """
    try:
        return float(a) * float(b)
    except ValueError:
        print("Invalid input. Please enter numeric values.")


if __name__ == "__main__":
    print("Welcome to Smart Calculator (Multiply Function)")
    x = input("Enter first number: ")
    y = input("Enter second number: ")
    result = multiply(x, y)
    print(f"The result is: {result}")
def add(a, b):
    return a + b