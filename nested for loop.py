for row in range(5):  # Outer loop for rows
    for col in range(5):  # Inner loop for columns
        # Check if the sum of the current row and column indices is even
        if (row + col) % 2 == 0:
            print('*', end=' ')  # Print an asterisk for even sums
        else:
            print('.', end=' ')  # Print a dot for odd sums
    print()  # Move to the next line after finishing a row 