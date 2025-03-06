#!/usr/local/bin/python3

#import libraries
import time
from file_integrity_monitoring import detect_file_changes
from process_monitoring import detect_suspicious_processes
from network_monitoring import monitor_network 
from log_analysis import analyze_logs
from alerting_system import send_email_alert

#main function 
def run_hids():
    while True:
        output1 = detect_file_changes()
        output2 = detect_suspicious_processes()
        output3 = monitor_network()
        output4 = analyze_logs()

        if output1 is not None or output2 is not None or output3 is not None or output4 is not None:
            send_email_alert('HOST IDS ALERT', 'Suspicious activity detected on your system!')
        
        time.sleep(60) #Runs every 60 seconds 

if __name__ == '__main__':
    run_hids()