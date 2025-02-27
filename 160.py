import socket
import smtplib
import uuid
import os
from email.mime.text import MIMEText
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse as urlparse

# Configuration
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
SMTP_USERNAME = 'your-email@example.com'
SMTP_PASSWORD = 'your-email-password'
EMAIL_FROM = 'your-email@example.com'
CONTENT_DIR = 'published_content'
TRACKING_FILE = 'link_tracking.txt'

# Ensure directories exist
os.makedirs(CONTENT_DIR, exist_ok=True)

def generate_unique_id(user_id):
    # Generate a unique ID based on user ID and current network information
    unique_id = f"{user_id}_{socket.gethostbyname(socket.gethostname())}_{uuid.uuid4()}"
    return unique_id

def send_confirmation_email(user_email, confirmation_link):
    msg = MIMEText(f"Please confirm your content by clicking the link: {confirmation_link}")
    msg['Subject'] = 'Confirm Your Content'
    msg['From'] = EMAIL_FROM
    msg['To'] = user_email

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.sendmail(EMAIL_FROM, [user_email], msg.as_string())

def create_confirmation_link(user_id, content):
    unique_id = generate_unique_id(user_id)
    confirmation_link = f"http://localhost:8000/confirm?uid={unique_id}&content={urllib.parse.quote(content)}"
    
    # Save the tracking info
    with open(TRACKING_FILE, 'a') as f:
        f.write(f"{unique_id}\t{user_id}\t{content}\t\n")

    return confirmation_link

def mark_content_as_published(unique_id):
    # Load existing tracking info
    with open(TRACKING_FILE, 'r') as f:
        lines = f.readlines()

    with open(TRACKING_FILE, 'w') as f:
        published = False
        for line in lines:
            uid, user_id, content, _ = line.strip().split('\t')
            if uid == unique_id:
                # Mark as published
                filename = os.path.join(CONTENT_DIR, f"{user_id}.txt")
                with open(filename, 'w') as content_file:
                    content_file.write(content)
                f.write(f"{uid}\t{user_id}\t{content}\t1\n")  # Mark as accessed
                published = True
            else:
                f.write(line)

    return published

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)
        query_params = urlparse.parse_qs(parsed_path.query)

        if 'uid' in query_params and 'content' in query_params:
            unique_id = query_params['uid'][0]
            content = urllib.parse.unquote(query_params['content'][0])

            if mark_content_as_published(unique_id):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"Content published successfully!")
            else:
                self.send_response(400)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b"Invalid or expired link.")
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Resource not found.")

def run_server():
    server_address = ('', 8000)
    http_server = HTTPServer(server_address, RequestHandler)
    print("Starting server on port 8000...")
    http_server.serve_forever()

if __name__ == "__main__":
    # Example usage
    user_id = "user123"
    user_email = "user@example.com"
    content = "This is the content to be published."

    confirmation_link = create_confirmation_link(user_id, content)
    send_confirmation_email(user_email, confirmation_link)

    # Run the server to handle confirmation requests
    run_server()