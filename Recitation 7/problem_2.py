def calcDet(matrix):
    # Calculate the determinant of a 2x2 matrix
    a, b = matrix[0][0], matrix[0][1]
    c, d = matrix[1][0], matrix[1][1]
    return a * d - b * c

def inverse(matrix):
    # Calculate the inverse of a 2x2 matrix using calcDet
    det = calcDet(matrix)
    
    a, b = matrix[0][0], matrix[0][1]
    c, d = matrix[1][0], matrix[1][1]
    # The inverse matrix formula
    inverse_matrix = [
        [d / det, -b / det],
        [-c / det, a / det]
    ]
    return inverse_matrix

def main():
    # Example 2x2 matrix
    matrix = [
        [4, 7],
        [2, 6]
    ]
    
    # Calculate determinant
    det = calcDet(matrix)
    print("Determinant:", det)
    
    # Calculate inverse
    inv_matrix = inverse(matrix)
    print("Inverse Matrix:")
    for row in inv_matrix:
        print(row)
    

# Run the main function
main()