import xml.etree.cElementTree as etree
import urllib.request
import urllib.response
import html.parser

from bs4 import BeautifulSoup

htmlparser = html.parser.HTMLParser()

class Runnable(object):

    def __init__(self) -> None:
        super().__init__()

    def run(self):
        pass

class Module(Runnable):

    def __init__(self, name: str) -> None:
        super().__init__()

        self._name = name
        self.options = []

    def show_options(self):
        pass

    def show_help(self):
        pass

    def react(self, input: str):
        pass

    def get_name(self):
        return self._name

    def set_name(self, name: str):
        self._name = name

    def get_option(self, index: int):
        return self.options[index]

    def set_option(self, index: int, val):
        self.options[index] = val

class Shell(Runnable):

    def __init__(self, prompt: str) -> None:
        super().__init__()

        self.PROMPT = prompt
        self.module_name = None
        self.module = None

    def react(self, input: str):
        pass

    def get_prompt(self):
        if self.module_name == None:
            return f"{self.PROMPT}>"
        else:
            return f"{self.PROMPT}({self.module_name})>"

    def back(self):
        if self.module_name != None:
            self.module_name = None

    def get_module(self) -> Module:
        return self.module


def parse(f: str):
    try:
        return etree.fromstring(f)
    except:
        debug("[!] Error while parsing...")

def check_ip_back(ip: str) -> bool:
    for i in ip.split(sep="."):
        if (int(i) >= 1 and int(i) <= 255):
            debug("" + i + " -> okay")
        else:
            print("[!] Unexpected input at '", i, "' in address")
            return False
    return True

def fetch_url(url: str):
    try:
        with urllib.request.urlopen(url) as response:
            return response.info()
    except:
        debug("[!] Error while fetching...")

def debug(msg: str) -> None:
    '''
    Prints the current Message as a debug-Message. This method is oly activated when the debug mode
    is enabled (do that with run or exploit -d)
    '''
    pass

def quit() -> None:
    print("Quitting...")
    sys.exit(0)

def parse_html(self, page) -> BeautifulSoup:
        debug("[*] Parsing...")
        s_soup = None
        try:
            s_soup = BeautifulSoup(page, "html.parser")   
        except:
            print("[!] Error while parsing the website")
            quit()
        debug("[*] Parsing complete.")
        return s_soup
