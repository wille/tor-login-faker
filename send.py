import socket
import requests
import socks
import stem.process
import hashlib
import os
import scraper
import random
import string

PANEL_URL = "http://localhost/login.php"
PORT = 5000
MAPFILE = "map.txt"

def randomPass():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))

def send():
    fingerprints = scraper.scrapeNodes()
    
    for fp in fingerprints:
        global tor_process
        print("Testing " + fp)
        
        try:
            tor_process = stem.process.launch_tor_with_config(
                config = {
                    'SocksPort': str(PORT),
                    'ExitNodes': fp,
                },
            )
                  
            password = randomPass()
                        
            data = {
                "user": "admin",
                "password": password
            }
            
            requests.get(PANEL_URL, data=data, timeout=10)
            
            print("Completed " + fp)
            
            tor_process.kill()
        except Exception as e: 
            print(str(e))
            tor_process.kill()

if __name__ == "__main__":
    send()