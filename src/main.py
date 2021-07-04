from fsradio.base import core, pin, exec

class MainShell(core.Shell):
    def __init__(self, prompt: str) -> None:
        super().__init__(prompt)

        self.modules = self.create_modules()

    def create_modules(self) -> list:
        return [exec.ExecModule(), pin.PinModule()]

    def run(self):
        while 1:
            inp = input(self.get_prompt())

            if inp != None:
                self.react(inp)

    def react(self, input: str):
        if not self.get_module():
            a = input.split(" ")
            if a[0] == "use":
                new_m = self.load(a[1])
                if new_m:
                    self.module = new_m
                    self.module_name = new_m.get_name()
                else:
                    print("[*] Unkown module!\n")
            elif a[0] == "quit":
                quit()
            elif a[0] == "modules":
                self.print_modules()

        else:
            if input.split(" ")[0] == "back":
                self.module = None
                self.module_name = None
            else:
                self.get_module().react(input)
                
    def load(self, name: str) -> core.Module:
        if name != None:
            for m in self.modules:
                if m.get_name() == name:
                    return m
        return None

    def print_modules(self):
        print("\n[*] Printing all loaded modules")
        for module in self.modules:
            if module:
                print(module.get_name())

    

print(" _________________________________________")
print("| Abusing the FSAPI from Frontier-Silicon |")
print(" ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
shell = MainShell("fsradio")
shell.run()