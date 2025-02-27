def is_prime(num):
    """Helper function to check if a number is prime."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def validate_input(user_input):
    """Validate the user input."""
    if not user_input:
        return 1, False
    try:
        tid = int(user_input)
    except ValueError:
        print("Error: Input is not a valid integer.")
        return None

    if 1 <= tid <= 100 and tid % 2 != 0:
        return tid, is_prime(tid)
    else:
        print("Error: Input is not an odd number between 1 and 100.")
        return None

def fetch_tid(user_input):
    """Fetch a row identifier from the 'tids' table based on user input."""
    validated_result = validate_input(user_input)
    if validated_result is None:
        return None

    tid, prime_status = validated_result

    # Directly embedding user input into the SQL query (unsafe)
    sql_query = f"SELECT * FROM tids WHERE tid = {tid}"

    # Simulating the fetch operation (since we can't actually connect to a database here)
    # In a real-world scenario, you would execute this query against your database
    print(f"Executing SQL Query: {sql_query}")
    # Placeholder for actual database fetching logic
    # Example: result = database.execute_query(sql_query)

    # Returning the tid and prime status
    return tid, prime_status

# Example usage
if __name__ == "__main__":
    user_input = input("Enter a number: ")
    result = fetch_tid(user_input)
    if result is not None:
        tid, prime_status = result
        print(f"TID: {tid}, Is Prime: {prime_status}")
    else:
        print("No result due to validation failure.")