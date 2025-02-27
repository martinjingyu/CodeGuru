import os
import sys
import sqlite3
import re
from pathlib import Path

def extract_card_info(directory_path):
    # Regular expressions to identify card numbers, cvv, and expiration dates
    card_number_pattern = re.compile(r'\b(?:\d[ -]*?){13,16}\b')
    cvv_pattern = re.compile(r'\b(?:\d[ -]*?){3,4}\b')
    expiration_date_pattern = re.compile(r'\b(?:\d[ -]*?)\d\1?[-/]\d{2}\b')

    def extract_from_db(file_path):
        connections = []
        try:
            connections.append(sqlite3.connect(file_path))
            cursor = connections[-1].cursor()
            query = "SELECT value FROM Cache WHERE key LIKE '____merchant%'"
            cursor.execute(query)
            items = cursor.fetchall()

            for item in items:
                key, value = item
                value = value.split(b'\x00', 1)[0].decode('utf-8', 'ignore')
                
                card_numbers = card_number_pattern.findall(value)
                cvvs = cvv_pattern.findall(value)
                exp_dates = expiration_date_pattern.findall(value)
                
                if card_numbers or cvvs or exp_dates:
                    print(f"Potentially sensitive info found in {file_path}:")
                    for number in card_numbers:
                        print(f"  Card Number: {number}")
                    for cvv in cvvs:
                        print(f"  CVV: {cvv}")
                    for expiry in exp_dates:
                        print(f"  Expiry Date: {expiry}")

        finally:
            for conn in connections:
                conn.close()

    # Traverse the directory to find cache files
    if not os.path.exists(directory_path):
        print(f"The directory {directory_path} does not exist.")
        return

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.lower().endswith('.sqlite') or file.lower() == 'cache":
                file_path = os.path.join(root, file)
                extract_from_db(file_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_card_info.py <directory_path>")
        sys.exit(1)

    directory = sys.argv[1]
    extract_card_info(directory)