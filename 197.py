def run_script_with_config(config, script):
    # Create a local environment for the script execution
    local_env = {}
    
    # Update the local environment with the configuration dictionary
    local_env.update(config)
    
    # Execute the script in the context of the local environment
    exec(script, {}, local_env)
    
    # Assuming the script defines a function or variable named 'result'
    # Return the result from the executed script
    return local_env.get('result')

# Example usage:
config = {
    'x': 10,
    'y': 5
}

script = """
def calculate():
    return x + y

result = calculate()
"""

result = run_script_with_config(config, script)
print(result)  # Output: 15