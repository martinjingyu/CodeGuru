def evaluate_expression():
    expression = input("Enter an arithmetic expression to evaluate: ")
    try:
        result = eval(expression)
        print(f"The result is: {result}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
# evaluate_expression()