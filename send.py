import socket
import requests
import socks
import stem.process
import hashlib
import os
import scraper
import random
import string
from queue import Queue
import threading
import tempfile

PANEL_URL = "http://localhost/login.php"
PORT = 5000
MAPFILE = "map.txt"
THREADS = 12

global queue
queue = Queue(maxsize=0)

def getaddrinfo(*args):
    return [(socket.AF_INET, socket.SOCK_STREAM, 6, '', (args[0], args[1]))]
    
def randomPass():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))

class sender(threading.Thread):
    
    def __init__(self, port):
        super(sender, self).__init__()
        self.port = port
        
        
    def run(self):                    
        config = queue.get()
        config["DataDirectory"] = tempfile.gettempdir() + os.pathsep + str(self.port)
        config["SocksPort"] = str(self.port)
        
        print("Testing " + config["ExitNodes"] + " on port " + str(self.port))

        try:
            tor_process = stem.process.launch_tor_with_config(config)
                      
            password = randomPass()
                            
            data = {
                "user": "admin",
                "password": password
            }
            
            socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", self.port)
            socket.socket = socks.socksocket

            socket.getaddrinfo = getaddrinfo
            socket.setdefaulttimeout(10)
                
            print("Content: " + requests.get(PANEL_URL, data=data, timeout=5).content.decode())
                                                
            tor_process.kill()
        except Exception as e: 
            print(str(e))
                
        file.close()

if __name__ == "__main__":
    fingerprints = scraper.scrapeNodes()

    file = open(MAPFILE, mode="a")

    for fingerprint in fingerprints:
        password = randomPass()

        file.write(fingerprint + "=" + password + os.linesep)

        config = {
            "ExitNodes": fingerprint
        }
        queue.put(config)

    file.close()

    for i in range(0, THREADS):
        thread = sender(PORT + i)
        thread.start()
    
    
    queue.join()    
