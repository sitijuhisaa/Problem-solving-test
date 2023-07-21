def is_balanced_bracket(s):
    stack = []
    opening_brackets = "([{"
    closing_brackets = ")]}"

    for char in s:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return "NO"
            top = stack.pop()
            if (char == ")" and top != "(") or \
               (char == "]" and top != "[") or \
               (char == "}" and top != "{"):
                return "NO"

    return "YES" if not stack else "NO"

# Contoh penggunaan fungsi
sample_input_1 = "{[()]}"
sample_input_2 = "{[(])}"
sample_input_3 = "{(([])[])[]}"

print(is_balanced_bracket(sample_input_1))  # Output: YES
print(is_balanced_bracket(sample_input_2))  # Output: NO
print(is_balanced_bracket(sample_input_3))  # Output: YES
