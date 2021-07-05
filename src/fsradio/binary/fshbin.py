import abc
from os import abort
import sys

from string import digits
from fsradio.base.core import BaseModule, error, log, nonNull

hui = [239, 191, 189, ]

escape = [
    '#', '"', '@', '=', '}', '[', ']', '{', '^', '>', '<', 
    '&', '%', '$', '~', ';', '!', '`', ',', '/', '(', ')',
    '*', '|', '\'', '\\', '+']

EOF = "xX"

class FSBinaryModule(BaseModule):
    def __init__(self, ) -> None:
        super().__init__("/binay/fsh_system", 1)

        self.PATH = 0

    def _set_(self, a: str):
        if a[1] in ["PATH", "path"]:
            self.set_option(0, str(a[2])) # '0' for self.PATH
            print(" " + f"PATH → {self.get_option(0)}\n")
        else:
            error("Unknown command\n")

    def run(self):
        print()
        if not nonNull(self.get_option(0)):
            error("Cannot start without a file\n")
            return

        data = open(self.get_option(0), "rb")
        if not data:
            error("File dos not exists!\n")   
            return

        def find(file) -> list:
            by = file.read()
            found = ""
            strings = []
            for x in by:
                if x in hui:
                    if len(found) > 1:
                        strings.append(found)
                        found = ""
                else:
                    if 32 <= x <= 126:
                        if chr(x) not in escape:
                            found += chr(x)
                    else:
                        if len(found) > 1:
                            strings.append(found)
                            found = ""
            return strings

        values = find(data)

        index = 0
        amount = 0
        for nop in values:
            if nop:
                if "FSH" in nop:
                    amount += 1
                    print(nop + "\n")
            if amount == 2:
                break
            index += 1
        if amount == 1:
            index = 0
        elif amount == 2:
            pass
        else:
            error("Could not resolve file.\n")
            return
        print(f" ┌── File-System: {values[index]}, Size: {values[index + 1]}")

        i = index + 2
        name = ""
        while 1:# TRUE could also be used here
            name = values[i]
            c = '├'

            while True:
                next = values[i+1]
                if '.' in next:
                    c = '├'
                    break
                else:
                    for x in next:
                        if x in digits:
                            name += f", Size: {next}"
                            i += 1
                            c = '├'
                            break
                    c = '└'
                    break
                
            if '.' in name:
                print(f" │  {c}── " + name)
                a = name.split(" ")
                if "bin" in a[len(a) - 1]:
                    print(" └── EOF → only compressed data follows")
                    break
            elif name == "LICENSE":
                print(" │  ├── " + name)
            elif name == EOF:
                print(" └── EOF → only compressed data follows :: " + name)
                break
            else: #new folder
                if name == "fK":
                    print(" │ ")
                    print(" ├──┬─ "+ name + "/ [Folder could also be 'web']")
                else:
                     print(" │ ")
                    print(" ├──┬─ "+ name + "/")
            i +=1
        print()

    def show_options(self):
        l_option = self.len_of(["path", "option"])
        l_required = self.len_of(["yes", "no", "Required"])
        l_value = self.len_of([self.get_option(0), "value"])

        self.print_table(l_option, l_required, l_value, 
                        [["OPTION", "REQUIRED", "VALUE"],
                        ["PATH", "yes", self.get_option(0)]])