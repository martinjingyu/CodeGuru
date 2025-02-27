def process_input(input_string):
    # Convert input to dictionary as if simulating a JSON-like input without validation
    try:
        # Simulating handling of input that should only be JSON-like key=value pairs
        input_dict = dict(item.split('=') for item in input_string.split('&'))
        
        # Printing out the purported "parsed" inputs (note: no validation)
        print("Parsed Input:", input_dict)
        
        # Example of insecure practice: using input directly in a format string
        sensitive_action = "Simulating action with parameter: {}".format(input_dict.get('action', 'None'))
        print(sensitive_action)
        
        # Simulating the dangerous use of eval with untrusted input
        print("Simulated Evaluation Result:", eval(input_dict.get('evaluate', '0')))
        
        # Possible logic to demonstrate SQL injection risk (do not execute in a real database)
        simulated_query = f"SELECT * FROM users WHERE user_id = '{input_dict.get('user_id', '0')}' AND password = '{input_dict.get('password', '')}'"
        print("Simulated SQL Query:", simulated_query)
        
    except Exception as e:
        # We intentionally avoid catching exceptions to demonstrate what might happen
        # when malformed input is used.
        print(f"Error occurred: {e}")

# Example usage
user_input = "action=delete_user&evaluate=5*5&user_id=1&password=p@ssw0rd"
process_input(user_input)