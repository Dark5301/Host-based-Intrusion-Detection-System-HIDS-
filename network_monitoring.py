#!/usr/local/bin/python3
import psutil 
import hids_logger as logger

def monitor_network():
	suspicious_ips = ['45.227.253.200', '185.220.201.182', '209.141.45.27', '193.32.163.123', '141.98.218.42']
	for conn in psutil.net_connections(kind='all'):
		if conn.raddr and conn.raddr[0] in suspicious_ips:
			alert_message = f'[ALERT] connection to suspicious IP: {conn.raddr[0]}'
			logger.log_event(alert_message)
			return alert_message
	return None

monitor_network()