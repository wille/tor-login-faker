# tor-login-faker

Posts fake unique login information to a fake website/server over an unencrypted connection through all possible tor exit nodes, and later waits for login attempt with these unique credentials and detects which exit node that sniffed the traffic

## Modules

- HTTP POST login to fake website

### Planned modules

- FTP
- IMAP

## Requirements

- requests, pysocks and stem, can be installed using "pip install requests stem pysocks"
- Python 3

## Thanks to

@intchloe idea and base [Don't touch my binary](https://github.com/intchloe/Don-t-touch-my-bin-/)
