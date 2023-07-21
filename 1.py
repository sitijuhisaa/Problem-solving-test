def A000124(n):
    if n < 1:
        raise ValueError("n harus lebih besar dari atau sama dengan 1")
    return n ** 2

def solve_A000124(input_number):
    if input_number < 1:
        raise ValueError("Input harus lebih besar dari atau sama dengan 1")

    sequence = []
    current_number = 0

    for i in range(1, input_number + 1):
        current_number += i
        sequence.append(A000124(current_number))

    return sequence

input_value = 4
output_sequence = solve_A000124(input_value)
print(output_sequence)
