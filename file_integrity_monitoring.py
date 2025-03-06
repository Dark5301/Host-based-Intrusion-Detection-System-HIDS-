#!/usr/local/bin/python3
import sys
import os
import hashlib
import hids_logger as logger

def get_file_hash(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        hasher.update(f.read())
    return hasher.hexdigest()

#Monitor critical system file 
file_hashes = {
    '/etc/passwd': get_file_hash('/etc/passwd'),
}

def detect_file_changes():
    for file, original_hash in file_hashes.items():
        current_hash = get_file_hash(file)
        if original_hash != current_hash:
            alert_message = f'[ALERT] ERROR: {file} has changed!'
            logger.log_event(alert_message)
            return alert_message 
    return None
            
        
detect_file_changes() 