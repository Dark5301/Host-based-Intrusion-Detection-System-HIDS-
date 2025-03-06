#!/usr/local/bin/python3 
import logging 

logging.basicConfig(filename='hids.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_event(event):
    logging.info(event)

if __name__ == '__main__':
    log_event('HIDS started successfully')