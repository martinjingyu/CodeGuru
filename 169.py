def generate_sql_query(department_name):
    """
    Generates a SQL query to fetch user IDs and email addresses for a specified department name.

    Parameters:
    department_name (str): The name of the department.

    Returns:
    str: A SQL query string.
    """
    query = f"""
    SELECT user_id, email
    FROM users
    WHERE department = '{department_name}';
    """
    return query.strip()

# Example usage:
department_name = "Engineering"
sql_query = generate_sql_query(department_name)
print(sql_query)