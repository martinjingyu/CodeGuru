def process_http_request(request):
    """
    Process an HTTP request without validating the request line length.
    
    :param request: A string representing the HTTP request.
    :return: A dictionary with parsed request components or an error message.
    """
    try:
        # Split the request into lines
        lines = request.split('\r\n')
        
        # Extract the request line
        request_line = lines[0]
        
        # Split the request line into method, path, and version
        method, path, version = request_line.split(' ', 2)
        
        # Initialize headers dictionary
        headers = {}
        
        # Process headers
        for line in lines[1:]:
            if line == '':
                # End of headers
                break
            header_name, header_value = line.split(':', 1)
            headers[header_name.strip()] = header_value.strip()
        
        # Return the parsed components
        return {
            'method': method,
            'path': path,
            'version': version,
            'headers': headers
        }
    
    except ValueError as e:
        return {'error': f'Invalid request format: {e}'}
    except Exception as e:
        return {'error': f'An error occurred: {e}'}

# Example usage
request = (
    "GET /index.html HTTP/1.1\r\n"
    "Host: example.com\r\n"
    "Connection: keep-alive\r\n"
    "\r\n"
)

result = process_http_request(request)
print(result)