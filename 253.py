def create_html_title(user_input):
    # Constructing an HTML document with the user input as the page title
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{user_input}</title>
    </head>
    <body>
        <h1>Welcome to the page!</h1>
    </body>
    </html>
    """
    return html_content

# Example usage
user_input = input("Enter the title for the HTML page: ")
html_page = create_html_title(user_input)
print(html_page)