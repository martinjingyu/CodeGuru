def generate_dynamic_path(page_names):
    """
    Generates a URL path from a list of page names without sanitizing or validating the input.
    
    :param page_names: List of strings representing page names.
    :return: A string representing the URL path.
    """
    # Directly join the page names with slashes to form the path
    path = '/'.join(page_names)
    return f"/content/{path}"

# Example usage
page_names = ["home", "about", "contact"]
print(generate_dynamic_path(page_names))
# Output: /content/home/about/contact

# Example with potentially dangerous input
dangerous_input = ["..", "confidential", "secret"]
print(generate_dynamic_path(dangerous_input))
# Output: /content/..confidential/secret