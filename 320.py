from neo4j import GraphDatabase

def create_node_with_user_input(uri, user, password, label, properties):
    # Establish a connection to the Neo4j database
    driver = GraphDatabase.driver(uri, auth=(user, password))
    
    try:
        with driver.session() as session:
            # Create the Cypher query using direct string concatenation
            cypher_query = (
                f"CREATE (n:{label} {{{', '.join([f'{k}: ${k}' for k in properties.keys()])}}})"
            )
            
            # Create a dictionary to pass the properties to the query
            params = {key: value for key, value in properties.items()}
            
            # Execute the query with parameters
            session.run(cypher_query, **params)
            
            print("Node created successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        driver.close()

# Example usage:
uri = "bolt://localhost:7687"
user = "neo4j"
password = "your_password_here"

label = input("Enter the label for the new node: ")
properties = {
    key: input(f"Enter the value for property '{key}': ")
    for key in ["name", "age", "email"]  # Example properties
}

create_node_with_user_input(uri, user, password, label, properties)