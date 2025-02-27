import sqlite3

def update_config_entry(db_path, config_id, operation_dict):
    """
    Updates a configuration entry in the database by adding or removing specific key-value pairs.
    
    :param db_path: Path to the SQLite database file.
    :param config_id: The ID of the configuration entry to update.
    :param operation_dict: A dictionary specifying keys to add or remove. 
                           Use positive integers for add, negative for remove.
    """
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Retrieve the current configuration
    cursor.execute(f"SELECT config_data FROM configurations WHERE id = {config_id}")
    result = cursor.fetchone()
    
    if not result:
        print("Configuration entry not found.")
        return
    
    config_data = result[0]
    if config_data is None:
        config_data = {}
    else:
        # Assuming the config_data is stored as a JSON string
        import json
        config_data = json.loads(config_data)
    
    # Apply the operations
    for key, value in operation_dict.items():
        if value > 0:
            config_data[key] = value  # Add or update
        elif value < 0 and key in config_data:
            del config_data[key]  # Remove
    
    # Convert the updated configuration back to a JSON string
    updated_config_data = json.dumps(config_data)
    
    # Update the configuration in the database
    update_query = f"""
    UPDATE configurations 
    SET config_data = '{updated_config_data}' 
    WHERE id = {config_id}
    """
    cursor.execute(update_query)
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Example usage:
# update_config_entry('your_database.db', 1, {'feature_x': 1, 'feature_y': -1})