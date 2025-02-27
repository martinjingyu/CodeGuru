from pymongo import MongoClient

def unsafe_mongo_query(mongo_uri, db_name, collection_name, filter_input, aggregation_pipeline=None):
    """
    An unsafe function that directly uses user-provided input to filter and aggregate documents 
    in a MongoDB collection without sanitization.

    Args:
    - mongo_uri (str): The connection URI for MongoDB.
    - db_name (str): The name of the database.
    - collection_name (str): The name of the collection.
    - filter_input (dict): A dictionary representing the filter query. Directly uses user input.
    - aggregation_pipeline (list): A list representing the aggregation pipeline stages. Directly uses user input.

    Returns:
    - dict: The result of the query as a dictionary.
    """
    # Connect to MongoDB
    client = MongoClient(mongo_uri)
    db = client[db_name]
    collection = db[collection_name]

    # Directly use filter_input without sanitization for filtering
    filtered_documents = list(collection.find(filter_input))

    if aggregation_pipeline:
        # Directly use aggregation_pipeline without sanitization for aggregation
        result = list(collection.aggregate(aggregation_pipeline))
        return {"aggregation_result": result}
    else:
        return {"filtered_documents": filtered_documents}

# Example usage (DO NOT use in production):
# result = unsafe_mongo_query(
#     'mongodb://localhost:27017',
#     'testdb',
#     'testcollection',
#     {'field': {'$gt': 'malicious_value'}},  # Malicious input example
#     [{'$group': {'_id': '$field', 'count': {'$sum': 1}}}])  # Untrusted aggregation pipeline
# print(result)