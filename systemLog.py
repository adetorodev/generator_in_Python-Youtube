import random
import datetime

def generate_random_log_entry():

    # Generate a random date and time within a certain range (for example, from 2020 to 2024)
    start_date = datetime.datetime(2020, 1, 1)
    end_date = datetime.datetime(2024, 12, 31)
    random_date = start_date + datetime.timedelta(
        seconds=random.randint(0, int((end_date - start_date).total_seconds()))
    )

    # List of possible error messages
    error_messages = [
        "Disk space is critically low.",
        "Unable to connect to the database.",
        "File not found: /var/log/syslog.",
        "Timeout while connecting to server.",
        "Memory allocation failed.",
        "Invalid user credentials provided.",
        "Error processing request at endpoint /api/users.",
        "Failed to load configuration file.",
        "Network connection dropped unexpectedly.",
        "Access denied: insufficient permissions."
    ]

    # Choose a random error message
    error_message = random.choice(error_messages)

    # Format the log entry
    log_entry = f"[{random_date.strftime('%Y-%m-%d %H:%M:%S')}] ERROR: {error_message}"

    return log_entry

# Example of generating multiple random log entries
for _ in range(5):
    print(generate_random_log_entry())
