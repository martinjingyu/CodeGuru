import pickle

def load_serialized_object(serialized_data):
    """
    Load a serialized object from a bytestring using pickle.loads.

    :param serialized_data: A bytestring containing the serialized object.
    :return: The reconstructed object.
    """
    if not isinstance(serialized_data, (bytes, bytearray)):
        raise TypeError("Input must be a bytestring.")

    return pickle.loads(serialized_data)

# Example usage:
# serialized = pickle.dumps({'key': 'value'})
# obj = load_serialized_object(serialized)
# print(obj)  # Output: {'key': 'value'}