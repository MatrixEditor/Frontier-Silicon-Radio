import requests

from fsradio.base import core
from fsradio.base.core import log, error

class FirmwareModule(core.BaseModule):
    def __init__(self) -> None:
        super().__init__("/scanner/firmware_downloader", 2)

        self.VERSION = 0
        self.PATH = 1

    def check(self, c):
        return c != None and c != ""

    def _set_(self, cmds):
        if cmds[1] == "VERSION":
            self.set_option(self.VERSION, str(cmds[2]))
            print(f"VERSION → {self.get_option(self.VERSION)}\n")
        elif cmds[1] == "PATH":
            self.set_option(self.PATH, str(cmds[2]))
            print(f"PATH → {self.get_option(self.PATH)}\n")
        else:
            error(f"Unexpected command: {cmds[1]}\n")

    def run(self):
        if not self.check(self.get_option(self.VERSION)):
            error(f"Cannot run without a Version number: {self.get_option(self.VERSION)}")
            return 

        if not self.check(self.get_option(self.PATH)):
            error(f"Cannot run without a path: {self.get_option(self.PATH)}")
            return 

        print()
        log("Creating URL...")
        URL_t = f"http://update.wifiradiofrontier.com/Update.aspx?f=/updates/"

        v = self.get_option(self.VERSION).split("_V")
        version = None
        if len(v) == 2: # everything is fine
            version = v[0] + "." + v[1] + ".isu.bin"
            URL_t += version
        else:
            log(f"Errr while resovling the version-number! >> '{self.get_option(self.VERSION)}'")

        log(f"Running with: {URL_t}")

        r = requests.get(URL_t, allow_redirects=True)
        log("Got a response!")
        log("Reading...")
        if r.text != None:
            log(f"Writing content to file...  ({self.get_option(self.PATH)}.isu.bin)")
            open(self.get_option(self.PATH) + ".isu.bin", "wb").write(r.content)
            log("Successfully written!\n")
        else:
            error("URL-Error: 'false url'")

    def show_options(self):
        l_option = self.len_of(["version", "path", "option"])
        l_required = self.len_of(["yes", "no", "Required"])
        l_value = self.len_of([self.get_option(self.VERSION), self.get_option(self.PATH), "value"])

        self.print_table(l_option, l_required, l_value, 
                        [["OPTION", "REQUIRED", "VALUE"],
                        ["VERSION", "yes", self.get_option(self.VERSION)],
                        ["PATH", "yes", self.get_option(self.PATH)]])