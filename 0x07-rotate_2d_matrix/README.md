#### Matrix Rotation

This program rotates an n x n 2D matrix 90 degrees clockwise in place.

#### Usage

The rotate_2d_matrix function takes one argument, matrix, which is a 2D matrix represented as a list of lists. The matrix must have two dimensions and must not be empty. The function modifies the matrix in place, without returning anything.


    from matrix_rotation import rotate_2d_matrix

#### Example matrix
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

#### Rotate the matrix
rotate_2d_matrix(matrix)

#### Print the rotated matrix
    for row in matrix:
        print(row)

    Output:

    [7, 4, 1]
    [8, 5, 2]
    [9, 6, 3]

#### Implementation

The rotate_2d_matrix function implements the following steps to rotate the matrix:

Transpose the matrix by swapping the values across the diagonal.
Reverse each row of the matrix.

### Authors & Contributers:
*kabingu Sammy* - [Github](https://github.com/kabingusam) || [twitter](https://twitter.com/Kabingusammy)

### Acknowledgments 
***
Alx SE Program.