# You need to create a custom logging module called logger.py 
# that can be imported and used in other Python files.
# Generate the current timestamp.
# Create a formatted log message.
# Display the message on the terminal.
# Save the same message into a file called app.log.

import os
from datetime import datetime

log_file = "app.log"

#helper function for printing log messages
def _log(level, message):
    timestamp = datetime.now()

    log_message = f"[{timestamp}] [{level:<7}] {message}"

    print(log_message)

    with open(log_file, "a") as file:
        file.write(log_message + "\n")


def info(message):
    _log("INFO", message)

def warning(message):
    _log("WARNING", message)

def error(message):
    _log("ERROR", message)

def debug(message):
    _log("DEBUG", message)

#Reading the logs from file based on filter
def read_logs(level_filter = None):
    if not os.path.exists(log_file):
        return []


    with open(log_file, "r") as file:
        lines = file.readlines()
        all_logs = []
        if level_filter == None:
            for line in lines:
                all_logs.append(line.strip())
            return all_logs
        
        filtered_logs = []
        
        for line in lines:
            if f"[{level_filter}" in line:
                filtered_logs.append(line.strip())

        return filtered_logs

