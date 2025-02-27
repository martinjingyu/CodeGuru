def execute_user_input():
    user_input = input("Enter a Python expression or statement: ")
    result = eval(user_input)
    print(f"Result: {result}")

# Execution
execute_user_input()