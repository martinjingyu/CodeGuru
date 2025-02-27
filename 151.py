def generate_sql_query(group_name):
    """
    Generates a SQL query to retrieve host IDs and hostnames for a specified network group.

    Parameters:
    group_name (str): The name of the network group.

    Returns:
    str: A SQL query string.
    """
    # Construct the SQL query
    query = f"""
    SELECT host_id, hostname
    FROM hosts
    JOIN host_groups ON hosts.hostgroup_id = host_groups.id
    WHERE host_groups.name = '{group_name}';
    """

    return query

# Example usage:
group_name = "ExampleNetworkGroup"
sql_query = generate_sql_query(group_name)
print(sql_query)