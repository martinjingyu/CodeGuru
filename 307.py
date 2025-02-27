def process_user_query(user_input):
    """
    This function inserts user input directly into HTML content without sanitization or validation.
    WARNING: This is insecure and should never be used in a real-world application due to the risk of XSS.
    """
    # Unsafe HTML template
    html_template = f"""
    <html>
    <head>
        <title>User Query</title>
    </head>
    <body>
        <h1>User Input</h1>
        <p>{user_input}</p>
    </body>
    </html>
    """
    return html_template

# Example usage
user_input = "<script>alert('XSS Attack!');</script>"
unsafe_html = process_user_query(user_input)
print(unsafe_html)