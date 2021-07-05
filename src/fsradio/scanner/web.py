from fsradio.base import core
from fsradio.fsapi import pin
from fsradio.fsapi import exec
from fsradio.scanner import ware

from fsradio.base.core import log, error

class ResolveModule(core.BaseModule):
    def __init__(self) -> None:
        super().__init__("/scanner/web_scanner", 2)

        self.RHOST = 0
        self.PATH = 1
        self.pin_resolver = pin.PinModule()
        self.executor = exec.ExecModule()
        self.downloader = ware.FirmwareModule()

    def _set_(self, a: str):
        if a[1] == "RHOST":
            self.set_option(self.RHOST, str(a[2]))
            print(f"RHOST → {self.get_option(self.RHOST)}\n")
        elif a[1] == "PATH":
            self.set_option(self.PATH, str(a[2]))
            print(f"PATH → {self.get_option(self.PATH)}\n")
        else:
            error(f"Unexpected command: {a[1]}\n")

    def check(self, c):
        return c != None and c != ""

    def run(self):
        print("\n")
        print("┌────────────────────────────────────────┐")
        print("│  Collecting PIN, VERSION and Firmware  │")
        print("├───────────────────┬────────────────────┤")
        print(f"│  PATH             │  {self.convertPath(13)}  │")
        print(f"│  RHOST            │  {self.convertRHOST(16)}  │")
        print("└────────────────────────────────────────┘\n")
        if not self.check(self.get_option(self.PATH)):
            error(f"Cannot run without a Version number: {self.get_option(self.PATH)}")
            return 

        log("Status: resolving PIN...")
        self.pin_resolver.react(f"run -i {self.get_option(self.RHOST)} -d")
        pin = self.pin_resolver.PIN
        if pin:
            log("Status: loading version-number")
            self.executor.set_option(self.executor.COMMAND, "GET/netRemote.sys.info.version")
            self.executor.set_option(self.executor.RHOST, self.get_option(self.RHOST))
            self.executor.run()

            version = self.executor.CHILD_VALUE
            if version:
                log(f"Status: fetching firmware to '{self.get_option(self.PATH)}.isu.bin'")
                self.downloader.set_option(self.downloader.VERSION, version)
                self.downloader.set_option(self.downloader.PATH, self.get_option(self.PATH))
                self.downloader.run()
                log("Status: completed successfully!\n")
            else:
                error("Warning: no device-version-number could be found!")
        else:
            error("Warning: could not resolve PIN\n")

    def convertPath(self, amount: int) -> str:
        papth = self.get_option(self.PATH)[:amount]
        if len(papth) >= 13:
            return papth + "..."
        else:
            return papth + " "*(16 - len(papth))

    def convertRHOST(self, amount: int) -> str:
        rhost = self.get_option(self.RHOST)
        return rhost + " "*(amount - len(rhost)) 

    def show_options(self):
        l_option = self.len_of(["Rhost", "path", "option"])
        l_required = self.len_of(["yes", "no", "Required"])
        l_value = self.len_of([self.get_option(self.RHOST), self.get_option(self.PATH), "value"])

        self.print_table(l_option, l_required, l_value, 
                        [["OPTION", "REQUIRED", "VALUE"],
                        ["RHOST", "yes", self.get_option(self.RHOST)],
                        ["PATH", "yes", self.get_option(self.PATH)]])