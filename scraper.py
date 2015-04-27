import requests
import os

def scrapeNodes(amount=-1):
    r = requests.get("https://check.torproject.org/exit-addresses")

    fingerprints = []
    
    for l in r.content.decode().split("\n"):
        if l.startswith("ExitNode "):
            l = l[9:].strip()
            print("Found node " + l)
            fingerprints.append(l)
            
    return fingerprints
        
if __name__ == "__main__":
    fingerprints = scrapeNodes()
    
    with open("nodes.txt", mode="w") as file:
        for l in fingerprints:
            file.write(l + os.linesep)
            