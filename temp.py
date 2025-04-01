import os
import smtplib
import threading
from datetime import datetime, timedelta
from email.mime.text import MIMEText

LOG_FILE = 'user_activity.log'
SUMMARY_INTERVAL_SECONDS = 3600  # e.g., every hour
EMAIL_SENDER = 'your_email@example.com'
EMAIL_RECEIVER = 'admin@example.com'
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
EMAIL_PASSWORD = 'your_email_password'  # Use environment variable in production


def append_user_activity(user_id: str, action: str):
    """
    Appends a standardized log entry to the activity log file.
    """
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"{timestamp} - USER: {user_id} - ACTION: {action}"
    try:
        with open(LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(log_entry + '\n')
    except Exception as e:
        print(f"Error writing log entry: {e}")


def get_recent_logs(since_minutes: int = 60):
    """
    Returns log entries within the last `since_minutes`.
    """
    cutoff = datetime.now() - timedelta(minutes=since_minutes)
    entries = []
    try:
        with open(LOG_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    timestamp_str = line.split(' - ')[0]
                    timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
                    if timestamp > cutoff:
                        entries.append(line.strip())
                except Exception:
                    continue
    except FileNotFoundError:
        pass
    return entries


def send_email_summary(log_lines):
    """
    Sends the collected log summary via email.
    """
    if not log_lines:
        return  # nothing to send

    summary = "\n".join(log_lines)
    msg = MIMEText(summary)
    msg['Subject'] = f'User Activity Summary - {datetime.now().strftime("%Y-%m-%d %H:%M")}'
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)
    except Exception as e:
        print(f"Failed to send email summary: {e}")


def periodic_summary_task():
    """
    Periodically collect and send user activity summaries.
    """
    logs = get_recent_logs()
    send_email_summary(logs)
    threading.Timer(SUMMARY_INTERVAL_SECONDS, periodic_summary_task).start()


# Only run summary if script is main
if __name__ == "__main__":
    print("User activity logging started. Summary will be sent periodically.")
    periodic_summary_task()

    # Optional: simulate user input
    while True:
        user = input("User ID: ")
        action = input("Action: ")
        append_user_activity(user, action)
