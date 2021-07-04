from bs4 import BeautifulSoup

from fsradio.base.core import Module, check_ip_back, fetch_url, parse_html, quit

class PinModule(Module):

    def __init__(self) -> None:
        super().__init__("/fsapi/resolve_pin")

        self.cmd = None

    def run(self):
        '''
        @param: The -i flag indicates the ip-Address to connect to
        @param: The -d flag indicates if the debug should be enabled
        '''
        try:
            if self.get_command()[1] == "-i":
                ip = str(self.get_command()[2])

                if len(self.get_command()) > 3:
                    if self.get_command()[3] == "-d":
                        debug = lambda str: print(str)

                try:
                    check_ip_back(ip)
                except:
                    print("[!] Unexpected error at -i -> '", ip, "'")
                    quit()

                self.URL = "http://" + ip + "/web/iperf/control.html"  

                page = fetch_url(self.URL)
                soup = parse_html(page)

                try:
                    pins = soup.find(id="radiopintextarea")

                    pin_t = self.exctract(pins)
                    self.result(pin=pin_t, url=self.URL)
                except:
                    print("[!] Error while trying to get the PIN")
                else:
                    print("[!] Unexpected input: '" + self.get_command()[1] + "'")
        except:
            print("[!] Error while trying to execute!")

        

    def react(self, input: str):
        self.cmd = input.split(" ")
        self.run()

    def show_options(self):
        return super().show_options()

    def show_help(self):
        return super().show_help()

    def get_command(self):
        return self.cmd