import socket
import requests
import socks
import stem.process
import hashlib
import os
import scraper

def send():
    fingerprints = scraper.scrapeNodes()
    
    for fp in fingerprints:
        pass

if __name__ == "__main__":
    send()