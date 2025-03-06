#!/usr/local/bin/python3 
import re
import hids_logger as logger

log_file = '/Users/princesingh/Desktop/log.txt'

def analyze_logs():
    with open(log_file, 'r') as f:
        logs = f.readlines()

    for log in logs:
        if 'Failed password' in log or 'sudo' in log:
            alert_message = f'[ALERT] Suspicious activity detected: {log.strip()}'
            logger.log_event(alert_message)
            return alert_message
    return None

analyze_logs()