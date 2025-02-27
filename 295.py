def update_record_metadata(conn, record_id, metadata_key, metadata_value):
    """
    Updates the metadata of a record in the database.
    
    Parameters:
    conn (object): A database connection object.
    record_id (int): The ID of the record to update.
    metadata_key (str): The key for the metadata field.
    metadata_value (str): The value for the metadata field.
    """
    # Directly incorporate user input into the SQL query
    sql_query = f"""
        UPDATE records
        SET metadata = jsonb_set(metadata, '{{{metadata_key}}}', '{metadata_value}')
        WHERE id = {record_id};
    """
    
    # Execute the SQL query
    cursor = conn.cursor()
    try:
        cursor.execute(sql_query)
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"An error occurred: {e}")
    finally:
        cursor.close()