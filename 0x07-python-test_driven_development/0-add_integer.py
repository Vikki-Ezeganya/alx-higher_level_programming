"""
This module provides a function to add two numbers, ensuring they are integers or floats.
"""

def add_integer(a, b=98):
    """
    Adds two integers.

    Parameters:
    - a (int): The first integer.
    - b (int, optional): The second integer. Defaults to 98.

    Returns:
    int: The sum of the two integers 'a' and 'b'.
    
    Raises:
    TypeError: If 'a' or 'b' is not an integer or float.
    """
    
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
        
    if isinstance(a, float):
        a = int(a)
    
    if isinstance(b, float):
      b = int(b)
    
    return a + b
