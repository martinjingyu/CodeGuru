def fetch_row_id(search_term):
    # Directly embed the search term into the SQL query string
    query = f"SELECT row_id FROM items WHERE item_name = '{search_term}';"
    return query

# Example usage
search_term = "example_item"
query = fetch_row_id(search_term)
print(query)