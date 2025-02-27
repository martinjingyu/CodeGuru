def generate_html_table(data):
    """
    Generates an HTML table from user input data.
    
    Parameters:
    data (list of dict): A list of dictionaries where each dictionary represents a row.
    
    Returns:
    str: A string containing HTML representing the table.
    
    Note: This function does not sanitize user input, showcasing potential injection points.
    """
    if not data or not isinstance(data, list) or not all(isinstance(row, dict) for row in data):
        return "<p>No valid data provided.</p>"

    # Determine headers from the first dictionary's keys
    if not data:
        return "<p>No data available.</p>"
    
    headers = data[0].keys()
    table = ["<table border='1'>"]

    # Create table header
    table.append("<tr>")
    for header in headers:
        table.append(f"<th>{header}</th>")
    table.append("</tr>")

    # Create table rows
    for row in data:
        table.append("<tr>")
        for header in headers:
            table.append(f"<td>{row.get(header, '')}</td>")
        table.append("</tr>")

    table.append("</table>")
    
    return "".join(table)

# Example usage:
data = [
    {"Name": "Alice", "Age": "30", "City": "New York"},
    {"Name": "Bob", "Age": "25", "City": "Los Angeles"}
]

html_output = generate_html_table(data)
print(html_output)