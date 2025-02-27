def evaluate_expression(expression: str):
    """
    Evaluates a given Python expression provided as a string.

    Parameters:
    - expression (str): A string representing a valid Python expression.

    Returns:
    - The result of the evaluated expression.

    Note: This function is for learning purposes only. Using `eval()` on untrusted input
    can lead to security vulnerabilities.
    """
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return f"An error occurred during evaluation: {e}"

# Example usage:
# expression = "2 + 3 * 5"
# result = evaluate_expression(expression)
# print(result)  # Output: 17