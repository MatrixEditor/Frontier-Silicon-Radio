import fsradio.fsapi.exec as executors
import fsradio.base.core as core

from fsradio.base.core import BaseModule, log, error, nonNull, check_ip_back, parse

basic_commands = {
    "netRemote.airplay.clearPassword",
    "netRemote.airplay.setPassword",
    "netRemote.misc.fsDebug.component",
    "netRemote.misc.fsDebug.traceLevel",
    "netRemote.nav.action.dabPrune",
    "netRemote.nav.action.dabScan",
    "netRemote.nav.browseMode",
    "netRemote.nav.caps",
    "netRemote.nav.dabScanUpdate",
    "netRemote.nav.depth",
    "netRemote.nav.errorStr",
    "netRemote.nav.list",
    "netRemote.nav.numItems",
    "netRemote.nav.presets",
    "netRemote.nav.searchTerm",
    "netRemote.nav.state",
    "netRemote.nav.status",
    "netRemote.platform.softApUpdate.updateModeRequest",
    "netRemote.platform.softApUpdate.updateModeStatus",
    "netRemote.play.addPreset",
    "netRemote.play.addPresetStatus",
    "netRemote.play.caps",
    "netRemote.play.control",
    "netRemote.play.errorStr",
    "netRemote.play.feedback",
    "netRemote.play.frequency",
    "netRemote.play.info.album",
    "netRemote.play.info.artist",
    "netRemote.play.info.duration",
    "netRemote.play.info.grapicUri",
    "netRemote.play.info.name",
    "netRemote.play.info.text",
    "netRemote.play.position",
    "netRemote.play.rate",
    "netRemote.play.repeat",
    "netRemote.play.scrobble",
    "netRemote.play.serviceIds.dabEnsembleId",
    "netRemote.play.serviceIds.dabScids",
    "netRemote.play.serviceIds.dabServiceId",
    "netRemote.play.serviceIds.ecc",
    "netRemote.play.serviceIds.fmRdsPi",
    "netRemote.play.shuffle",
    "netRemote.play.shuffleStatus",
    "netRemote.play.signalStrength",
    "netRemote.play.status",
    "netRemote.sys.alarm.config",
    "netRemote.sys.alarm.configChanged",
    "netRemote.sys.alarm.duration",
    "netRemote.sys.alarm.snooze",
    "netRemote.sys.alarm.snoozing",
    "netRemote.sys.alarm.status",
    "netRemote.sys.audio.eqCustom.param0",
    "netRemote.sys.audio.eqCustom.param1",
    "netRemote.sys.audio.eqCustom.param2",
    "netRemote.sys.audio.eqCustom.param3",
    "netRemote.sys.audio.eqCustom.param4",
    "netRemote.sys.audio.eqLoudness",
    "netRemote.sys.audio.eqPreset",
    "netRemote.sys.audio.extStaticDelay"
    "netRemote.sys.audio.mute",
    "netRemote.sys.audio.mute",
    "netRemote.sys.audio.volume",
    "netRemote.sys.audio.volume",
    "netRemote.sys.caps.clockSourceList",
    "netRemote.sys.caps.fmFreqRange.lower",
    "netRemote.sys.caps.fmFreqRange.StepSize"
    "netRemote.sys.caps.fmFreqRange.upper",
    "netRemote.sys.caps.modes",
    "netRemote.sys.caps.utcSettingsList",
    "netRemote.sys.caps.validLang",
    "netRemote.sys.caps.volumeSteps",
    "netRemote.sys.cfg.irAutoPlayFlag",
    "netRemote.sys.clock.dateFormat",
    "netRemote.sys.clock.dst",
    "netRemote.sys.clock.localDate",
    "netRemote.sys.clock.localTime",
    "netRemote.sys.clock.mode",
    "netRemote.sys.clock.source",
    "netRemote.sys.clock.utcOffset",
    "netRemote.sys.info.controllerName"
    "netRemote.sys.info.dmruuid",
    "netRemote.sys.info.friendlyName", 
    "netRemote.sys.info.radioId",
    "netRemote.sys.info.radioPin",
    "netRemote.sys.info.version",
    "netRemote.sys.ipod.dockStatus",
    "netRemote.sys.isu.control",
    "netRemote.sys.isu.mandatory",
    "netRemote.sys.isu.softwareUpdateProgress",
    "netRemote.sys.isu.state",
    "netRemote.sys.isu.summary",
    "netRemote.sys.isu.version",
    "netRemote.sys.lang",
    "netRemote.sys.mode",
    "netRemote.sys.net.commitChanges", 
    "netRemote.sys.net.ipConfig.address",
    "netRemote.sys.net.ipConfig.dhcp",
    "netRemote.sys.net.ipConfig.dnsPrimary",
    "netRemote.sys.net.ipConfig.dnsSecondary",
    "netRemote.sys.net.ipConfig.gateway",
    "netRemote.sys.net.ipConfig.subnetMask",
    "netRemote.sys.net.keepConnected",
    "netRemote.sys.net.wired.interfaceEnable",
    "netRemote.sys.net.wired.macAddress",
    "netRemote.sys.net.wlan.connectedSSID", 
    "netRemote.sys.net.wlan.interfaceEnable", 
    "netRemote.sys.net.wlan.macAddress",
    "netRemote.sys.net.wlan.performFCC",
    "netRemote.sys.net.wlan.performWPS",
    "netRemote.sys.net.wlan.region",
    "netRemote.sys.net.wlan.regionFcc",
    "netRemote.sys.net.wlan.rssi",
    "netRemote.sys.net.wlan.selectAP", 
    "netRemote.sys.net.wlan.setAuthType", 
    "netRemote.sys.net.wlan.setEncType",
    "netRemote.sys.net.wlan.setPassphrase",
    "netRemote.sys.net.wlan.wpsPinRead",
    "netRemote.sys.power", 
    "netRemote.sys.rsa.publicKey", 
    "netRemote.sys.rsa.status",
    "netRemote.sys.sleep",
    "netRemote.sys.state",

    # only 'SET' below
    "netRemote.nav.action.navigate",
    "netRemote.nav.action.selectItem",
    "netRemote.nav.action.selectPreset"
}

multiroom_commands = {
    "netRemote.multiroom.caps.maxClients",
    "netRemote.multiroom.caps.protocolVersion",
    "netRemote.multiroom.client.mute0",
    "netRemote.multiroom.client.mute1",
    "netRemote.multiroom.client.mute2",
    "netRemote.multiroom.client.mute3",
    "netRemote.multiroom.client.status0",
    "netRemote.multiroom.client.status1",
    "netRemote.multiroom.client.status2",
    "netRemote.multiroom.client.status3",
    "netRemote.multiroom.client.volume0",
    "netRemote.multiroom.client.volume1",
    "netRemote.multiroom.client.volume2",
    "netRemote.multiroom.client.volume3",
    "netRemote.multiroom.device.clientIndex",
    "netRemote.multiroom.device.clientStatus",
    "netRemote.multiroom.device.listAll", # LIST_GET or LIST_GET_NEXT
    "netRemote.multiroom.device.listAllVersion",
    "netRemote.multiroom.device.serverStatus",
    "netRemote.multiroom.device.transportOptimisation",
    "netRemote.multiroom.group.addClient",
    "netRemote.multiroom.group.attachedClients",
    "netRemote.multiroom.group.becomeServer",
    "netRemote.multiroom.group.create",
    "netRemote.multiroom.group.destroy",
    "netRemote.multiroom.group.id",
    "netRemote.multiroom.group.masterVolume",
    "netRemote.multiroom.group.name",
    "netRemote.multiroom.group.removeClient",
    "netRemote.multiroom.group.state",
    "netRemote.multiroom.group.streamable"
}

spotify_commands = {
    "netRemote.spotify.bitRate",
    "netRemote.spotify.lastError",
    "netRemote.spotify.status",
    "netRemote.spotify.username",
}

iperf_commands = {
    "netRemote.test.iperf.commandline", # &SET with value=delete
    "netRemote.test.iperf.console",
    "netremote.test.iperf.execute" #SET
}

FS_OK           = "FS_OK"
FS_FAIL         = "FS_FAIL"
FS_PACKET_BAD   = "FS_PACKET_BAD"
FS_TIMEOUT      = "FS_TIMEOUT"
FS_NODE_BLOCKED = "FS_NODE_BLOCKED"

FS_NODE_DOES_NOT_EXISTS = "FS_NODE_DOES_NOT_EXIST"

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
                        if val == FS_FAIL:
                            print_f(f"/fsapi/{operation}/{op}", "404", length)

                        elif val == FS_PACKET_BAD:
                            print_f(f"/fsapi/{operation}/{op}", f"{operation} could be false operation", length)

                        elif val == FS_NODE_DOES_NOT_EXISTS:
                            print_f(f"/fsapi/{operation}/{op}", f"404 or false operation ({operation})", length)
                        
                        elif val == FS_TIMEOUT:
                            print_f(f"/fsapi/{operation}/{op}", "TIMEOUT - Host could be down at the moment", length)

                        elif val == FS_OK:
                            print_f(f"/fsapi/{operation}/{op}", "OK", length)

                        else:
                            print_f(f"/fsapi/{operation}/{op}", f"404 ({val})", length)
                else:
                    print_f(f"/fsapi/{operation}/{op}", f"404 - {operation} could be false operation", length)
            print(" └──" + "─"*length + "┘")
            print("\n")

        print()
        log("Printing 404 for not found...\n")
        run_list(basic_commands, rhost=rhost, pin=pin, operation=operation, cmd="Known FsAPI")
        print()
        run_list(multiroom_commands, rhost=rhost, pin=pin, operation=operation, cmd="Multiroom")
        print()
        run_list(spotify_commands, rhost=rhost, pin=pin, operation=operation, cmd="Spotify")
        run_list(iperf_commands, rhost=rhost, pin=pin, operation=operation, cmd="Iperf")

    def show_options(self):
        l_option = self.len_of(["Rhost", "pin", "operation", "option"])
        l_required = self.len_of(["yes", "no", "Required"])
        l_value = self.len_of([self.get_option(self.RHOST), self.get_option(self.PIN), self.get_option(self.OP), "value"])

        self.print_table(l_option, l_required, l_value, 
                        [["OPTION", "REQUIRED", "VALUE"],
                        ["RHOST", "yes", self.get_option(self.RHOST)],
                        ["PIN", "no", self.get_option(self.PIN)],
                        ["OPERATION", "no", self.get_option(self.OP)]])

    def show_help(self):
        return super().show_help()    

