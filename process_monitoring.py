#!/usr/local/bin/python3
import psutil
import hids_logger as logger

def detect_suspicious_processes():
    suspicious_keywords = ['nc', 'nmap', 'meterpreter', 'kali', 'metasploit', 'wireshark', 'john', 'hydra']
    for process in psutil.process_iter(attrs=['pid', 'name']):
        for keyword in suspicious_keywords:
            if keyword in process.info['name']:
                alert_message = f'[ALERT] Process {process.info["name"]} with PID {process.info["pid"]} found!'
                logger.log_event(alert_message)
                return alert_message
    return None 

detect_suspicious_processes()