def pascal_triangle(n):
    """ Returns a list of lists representing Pascal's triangle of n. """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the first row of Pascal's triangle

    for i in range(1, n):
        row = [1]  # Every row starts with 1
        prev_row = triangle[i - 1]
        for j in range(1, i):
            # Each element is the sum of the two elements directly above it
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)  # Every row ends with 1
        triangle.append(row)

    return triangle
