def execute_user_input(user_input):
    try:
        # Prepare a local scope to capture the execution result
        local_scope = {}
        
        # Use 'exec' to execute the code in the provided local scope
        exec(user_input, {}, local_scope)
        
        # Check if any single assignment was made
        if '__result__' in local_scope:
            return local_scope['__result__']
        
        # Try evaluating the input as an expression, capture the result
        try:
            result = eval(user_input, {}, local_scope)
            return result
        except:
            pass

    except Exception as e:
        # Print the exception or handle it accordingly
        print(f"An error occurred: {e}")

    return None

# Example usage:
print(execute_user_input("x = 10"))           # Outputs: None
print(execute_user_input("__result__ = x + 5")) # Outputs: None (but __result__ is in scope with value 15)
print(execute_user_input("5 + 3"))             # Outputs: 8