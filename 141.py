def filter_rows(condition, rows=None):
    if rows is None:
        # Sample list of dictionaries if no input is provided
        rows = [
            {'id': 1, 'name': 'Alice', 'age': 30},
            {'id': 2, 'name': 'Bob', 'age': 25},
            {'id': 3, 'name': 'Charlie', 'age': 35},
            {'id': 4, 'name': 'David', 'age': 40}
        ]

    # Function to safely evaluate conditions
    def evaluate_condition(row):
        try:
            # Use eval to evaluate the condition string
            return eval(condition, {}, row)
        except Exception as e:
            print(f"Error evaluating condition: {e}")
            return False

    # Filter rows based on the condition
    filtered_rows = [row for row in rows if evaluate_condition(row)]
    return filtered_rows

# Example usage
condition = "age > 30"
filtered = filter_rows(condition)
print(filtered)