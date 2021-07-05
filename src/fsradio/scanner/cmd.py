import fsradio.fsapi.exec as executors
import fsradio.base.core as core
import fsradio.base.commands as cmdprov

from fsradio.base.core import BaseModule, log, error, nonNull, check_ip_back, parse

class CommandResolverModule(BaseModule):
    def __init__(self) -> None:
        super().__init__("/scanner/command_scanner", 3)

        self.RHOST = 0
        self.PIN = 1
        self.OP = 2
        self.set_option(self.PIN, "1234")
        self.set_option(self.OP, "GET")

    def _set_(self, cmds: str):
        if cmds[1] == "RHOST":
            self.set_option(self.RHOST, str(cmds[2]))
            print(" " + f"RHOST → {self.get_option(self.RHOST)}\n")
        elif cmds[1] == "PIN":
            self.set_option(self.PIN, str(cmds[2]))
            print(f" PIN → {self.get_option(self.PIN)}\n")
        elif cmds[1] == "OP":
            self.set_option(self.OP, str(cmds[2]))
            print(f" OP → {self.get_option(self.OP)}\n")

    def run(self):
        if not nonNull(self.get_option(self.PIN)):
            error(f"Cannot run without a pin: {self.get_option(self.PIN)}")
            return

        print("\n [*] Checking IP-Address...")
        if not check_ip_back(self.get_option(self.RHOST)):
            error(f"Cannot run without a valid host: {self.get_option(self.RHOST)}")
            return

        rhost = self.get_option(self.RHOST)
        pin = self.get_option(self.PIN)
        operation = self.get_option(self.OP)

        def get_len_of(mklist: list):
                i = 0
                for attr in mklist:
                    s = "    /fsapi/GET/" + str(attr)
                    if len(s) > i:
                        i = len(s)
                return i + 5

        def print_f(link: str, code: str, l: int):
            first = f" ├─ {link}"
            last = f"│  {code}"
            print(first + " "*(l - len(link)) + last)

        def run_list(commands: list, rhost: str, pin="1234", operation="GET", cmd=""):
            URL_t = None
            length = get_len_of(commands)
            
            print(f" ┌── Testing commands of ({cmd}):\n │")
            print(" ├──" + "─"*length + "┐")
            for op in commands:
                URL_t = f"http://{rhost}/fsapi/{operation}/{op}?pin={pin}"

                page = core.fetch_url(URL_t)
                data = parse(page.text)

                if data != None:
                    for st in data.iter("status"): #only one element always
                        val = st.text
                        if val == cmdprov.FS_FAIL:
                            print_f(f"/fsapi/{operation}/{op}", "404", length)

                        elif val == cmdprov.FS_PACKET_BAD:
                            print_f(f"/fsapi/{operation}/{op}", f"{operation} could be false operation", length)

                        elif val == cmdprov.FS_NODE_DOES_NOT_EXISTS:
                            print_f(f"/fsapi/{operation}/{op}", f"404 or false operation ({operation})", length)
                        
                        elif val == cmdprov.FS_TIMEOUT:
                            print_f(f"/fsapi/{operation}/{op}", "TIMEOUT - Host could be down at the moment", length)

                        elif val == cmdprov.FS_OK:
                            print_f(f"/fsapi/{operation}/{op}", "OK", length)

                        elif val == cmdprov.FS_NODE_BLOCKED:
                            print_f(f"/fsapi/{operation}/{op}", "OK, but too low authorization level ", length)
                        else:
                            print_f(f"/fsapi/{operation}/{op}", f"404 ({val})", length)
                else:
                    print_f(f"/fsapi/{operation}/{op}", f"404 - {operation} could be false operation", length)
            print(" └──" + "─"*length + "┘")
            print("\n")

        print()
        log("Printing 404 for not found...\n")
        run_list(cmdprov.basic_commands, rhost=rhost, pin=pin, operation=operation, cmd="Known FsAPI")
        print()
        run_list(cmdprov.multiroom_commands, rhost=rhost, pin=pin, operation=operation, cmd="Multiroom")
        print()
        run_list(cmdprov.spotify_commands, rhost=rhost, pin=pin, operation=operation, cmd="Spotify")
        run_list(cmdprov.iperf_commands, rhost=rhost, pin=pin, operation=operation, cmd="Iperf")

    def show_options(self):
        l_option = self.len_of(["Rhost", "pin", "operation", "option"])
        l_required = self.len_of(["yes", "no", "Required"])
        l_value = self.len_of([self.get_option(self.RHOST), self.get_option(self.PIN), self.get_option(self.OP), "value"])

        self.print_table(l_option, l_required, l_value, 
                        [["OPTION", "REQUIRED", "VALUE"],
                        ["RHOST", "yes", self.get_option(self.RHOST)],
                        ["PIN", "no", self.get_option(self.PIN)],
                        ["OPERATION", "no", self.get_option(self.OP)]])

