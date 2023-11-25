def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Parameters:
    - matrix (list of lists): The matrix containing numerical elements.
    - div (int or float): The divisor used to divide all elements of the matrix.

    Returns:
    list of lists: A new matrix with elements divided by the divisor and rounded to 2 decimal places.

    Raises:
    TypeError: If matrix is not a list of lists containing only integers or floats,
               or if the div is not a number (integer or float).
    ZeroDivisionError: If the divisor is zero.
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    result_matrix = []
    for row in matrix:
        new_row = [round(elem / div, 2) for elem in row]
        result_matrix.append(new_row)

    return result_matrix
