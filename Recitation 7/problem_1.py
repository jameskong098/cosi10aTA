def calcDet(matrix):
    # Calculate the determinant of a 2x2 matrix
    a, b = matrix[0][0], matrix[0][1]
    c, d = matrix[1][0], matrix[1][1]
    return a * d - b * c

def main():
    # Example 2x2 matrix
    matrix = [
        [4, 7],
        [2, 6]
    ]
    
    # Calculate determinant
    det = calcDet(matrix)
    print(f"Determinant: {det}")
    
# Run the main function
main()