import ctypes
import sys
import os

def load_and_execute_dll(dll_path, func_name, func_args):
    """
    Loads a DLL and executes a specified function within it.
    
    :param dll_path: Path to the DLL file.
    :param func_name: Name of the function to call from the DLL.
    :param func_args: Arguments to pass to the function.
    """
    # Check if the DLL exists
    if not os.path.exists(dll_path):
        print(f"Error: The file {dll_path} does not exist.")
        return

    # Load the DLL
    try:
        dll = ctypes.WinDLL(dll_path)
    except Exception as e:
        print(f"Error loading the DLL: {e}")
        return

    # Get the desired function from the DLL
    try:
        func = getattr(dll, func_name)
    except AttributeError:
        print(f"Error: Function {func_name} not found in the DLL.")
        return

    # Define the argument and return types for the function
    # This needs to be adjusted based on the actual DLL function signature
    # Example: if the function returns an int and takes an int and a float:
    # func.restype = ctypes.c_int
    # func.argtypes = [ctypes.c_int, ctypes.c_float]

    # Set the argument and return types (adjust as needed)
    # Example:
    # func.restype = ctypes.c_int
    # func.argtypes = [ctypes.c_int, ctypes.c_float]

    # Call the function
    try:
        result = func(*func_args)
        print(f"Function {func_name} executed successfully. Result: {result}")
    except Exception as e:
        print(f"Error executing function {func_name}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python script.py <path_to_dll> <function_name> <arg1> <arg2> ...")
        sys.exit(1)

    dll_path = sys.argv[1]
    func_name = sys.argv[2]
    func_args = [eval(arg) for arg in sys.argv[3:]]

    load_and_execute_dll(dll_path, func_name, func_args)