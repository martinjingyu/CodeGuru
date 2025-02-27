import psycopg2
import requests
import json

def log_connection_params(params, logging_endpoint):
    """Logs connection parameters to an external monitoring service."""
    try:
        response = requests.post(logging_endpoint, json=params)
        if response.status_code == 200:
            print("Connection parameters logged successfully.")
        else:
            print("Failed to log connection parameters.")
    except Exception as e:
        print(f"An error occurred while logging: {e}")

def connect_to_postgres(host, port, dbname, user, password, logging_endpoint):
    """Connects to a PostgreSQL database and logs connection parameters."""
    # Prepare connection parameters
    conn_params = {
        'host': host,
        'port': port,
        'dbname': dbname,
        'user': user,
        'password': password
    }
    
    # Log connection parameters
    log_connection_params(conn_params, logging_endpoint)
    
    # Attempt to connect to the PostgreSQL database
    try:
        cnx = psycopg2.connect(**conn_params)
        print("Connected to the database successfully.")
        return cnx
    except psycopg2.DatabaseError as e:
        print(f"Could not connect to the database: {e}")
        return None

# Example usage
logging_endpoint = "https://your-logging-endpoint.com/log"
connect_to_postgres("host_address", 5432, "scholars", "tblstore", "your_password", logging_endpoint)