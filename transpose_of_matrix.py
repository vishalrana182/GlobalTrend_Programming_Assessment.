def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0
    transpose = []
    for col in range(cols):
        transpose_row = []
        for row in range(rows):
            transpose_row.append(matrix[row][col])
        transpose.append(transpose_row)
    return transpose


def main():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Enter element at position ({i + 1}, {j + 1}): "))
            row.append(element)
        matrix.append(row)

    transposed_matrix = transpose_matrix(matrix)

    print("\nOriginal Matrix:")
    for row in matrix:
        print(row)

    print("\nTransposed Matrix:")
    for row in transposed_matrix:
        print(row)


if __name__ == "__main__":
    main()
