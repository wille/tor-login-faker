import requests

def scrapeNodes(amount=-1):
    r = requests.get("https://check.torproject.org/exit-addresses", timeout=15)

    fingerprints = []
    
    for l in r.content.split("\n"):
        if l.startswith("ExitNode "):
            l = l[10:]
            print("Found node " + l)
            fingerprints.append(l)
            
    return fingerprints
        
if __name__ == "__main__":
    scrapeNodes()