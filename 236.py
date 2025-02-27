import pickle

def deserialize_data(byte_stream):
    """
    Deserialize data from a byte stream using pickle.loads().
    
    :param byte_stream: A byte stream containing pickled data.
    :return: The deserialized object.
    """
    return pickle.loads(byte_stream)

# Example usage:
# byte_data = pickle.dumps(some_object)
# deserialized_object = deserialize_data(byte_data)