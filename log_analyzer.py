import pandas as pd
import numpy as np
import re

def parse_logs(file_path):
    """Parse the log file and return a DataFrame."""
    with open(file_path, 'r') as file:
        logs = file.readlines()

    log_entries = []
    for log in logs:
        log_entry = re.split(r'\s+', log.strip())
        log_entries.append(log_entry)

    df = pd.DataFrame(log_entries, columns=["Timestamp", "Source", "Message"])
    return df

def detect_incidents(df):
    """Detect potential security incidents in the log data."""
    incidents = df[df['Message'].str.contains('ERROR|ALERT', case=False, na=False)]
    return incidents

def main(file_path):
    df = parse_logs(file_path)
    incidents = detect_incidents(df)
    print("Detected Incidents:")
    print(incidents)

if __name__ == "__main__":
    file_path = 'sample_logs.txt'  # Replace with your log file path
    main(file_path)

