from bs4 import BeautifulSoup

from fsradio.base.core import Module, check_ip_back, error, fetch_url, parse_html, quit

class PinModule(Module):
    def __init__(self) -> None:
        super().__init__("/fsapi/resolve_pin")

        self.cmd = None
        self.PIN = None

    def debug(msg: str):
        pass

    def run(self):
        """
        @param: The -i flag indicates the ip-Address to connect to
        @param: The -d flag indicates if the debug should be enabled
        """
        if self.get_command()[1] == "-i":
            ip = str(self.get_command()[2])

            if len(self.get_command()) > 3:
                if self.get_command()[3] == "-d":
                    self.debug = lambda str: print(" " + str)

            try:
                print("\n [*] Checking IP-Address...")
                check_ip_back(ip)
            except:
                print(" [!] Unexpected error at -i -> '", ip, "'")
                quit()

            self.URL = "http://" + ip + "/web/iperf/control.html"

            page = fetch_url(self.URL)
            if page:
                soup = parse_html(page.text)

                try:
                    pins = soup.find(id="radiopintextarea")

                    pin_t = self.exctract(pins)
                    self.result(pin=pin_t, url=self.URL)
                    self.PIN = pin_t
                except:
                    print(" [!] Error while trying to get the PIN")
            else:
                error("Aborting to get the PIN...")
            
        elif self.get_command()[1] == "-w":
            pass # write to...
        else:
            print(" [!] Unexpected input: '" + self.get_command()[1] + "'")

    def react(self, input: str):
        self.cmd = input.split(" ")
        self.run()

    def exctract(self, pin: str) -> str:
        pin_t = str(pin)
        pin_t = pin_t[pin_t.index('>') + 1:]
        pin_t = pin_t[:pin_t.index('<')]
        return pin_t.strip()

    def result(self, pin: str, url: str) -> None:
        print("\n [#] Found PIN")
        print(" [#] WEB: " + url)
        print(" [#] PIN: " + pin + "\n")

    def show_options(self):
        print(" Please read documentation for options")

    def get_command(self):
        return self.cmd
