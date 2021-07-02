import sys
import requests

from requests.models import Response

def debug(msg: str):
    pass

def quit() -> None:
    print("Quitting...")
    sys.exit(0)

def fetch_url(url: str) -> Response:
        res = None
        debug("[*] Fetching URL...")
        try:
            res = requests.get(url)
        except:
            debug("[!] Error while fetching the URL")
            quit()
        debug("[*] Loading website ('" + url + "') completed.")
        return res

def check_ip(ip: str):
        debug("\n[*] Checking ip-address...")
        for i in ip.split(sep="."):
            if (int(i) >= 1 and int(i) <= 255):
                debug("" + i + " -> okay")
            else:
                print("[!] Unexpected input at '", i, "' in address")
                quit()
        debug("\n")

def check_ip_back(ip: str) -> bool:
    for i in ip.split(sep="."):
        if (int(i) >= 1 and int(i) <= 255):
            debug("" + i + " -> okay")
        else:
            print("[!] Unexpected input at '", i, "' in address")
            return False
    return True