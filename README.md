# MEDION MD87805

## Web-FsAPI
-----------

Diese API ist in vielen IoT-Geräten von Frontier-Silicon (auch Frontier-Smart) integriert und bietet die Möglichkeit, ohne eine Authentifizierung (okay, man braucht eine PIN) System-Calls über den Web-Browser auszuführen.

Um die Python3-Skripte auszuführen, empfiehlt es sich die beiden Bibliotheken BeautifulSoup4 und Response zu installieren:

    python -m pip install beautifulsoup4 
und:

    python -m pip install requests

 
 ## fsapi-Dokumentation
 ----------
[Hier](https://github.com/flammy/fsapi/blob/master/FSAPI.md) gibt es eine generelle API-Dokumentation zur fsapi.


## Main-Datei
-------------
Um das System zu starten, in der Konsole py, python3 oder python mit dem entsprechenden Datei-Namen angeben und _Enter_ drücken.

Danach können nur noch die Befehle _use_, _quit_ und _modules_ benutzt werden:

    * use [module-name] : nutzt das angegebene modul (die Namen der Module können mit 'modules' ausgegeben werden)
    * modules : gibt die Namen aller geladenen Module aus
    * quit : beendet das Programm

Wählt man nun ein Modul aus, wird dies im Konsolen-Prompt mit angegeben. Jetzt können nur noch die Befehle _set_, _run_, _show__options_ und _back_ benutzt werden:

    * set [option] [value] : Setzt die gewählte Option auf den gegebenen Wert
    * show options : gibt eine Liste mit allen nötigen Parametern aus
    * run : startet das modul
    * back : geht in das Startmenü zurück.

## Module
-----------

    * /fsapi/resolve_pin : Verucht die PIN eines Gerätes herauszufinden (Syntax: run -i <IP> [-d Optional für Debug-Mode]). Bei diesem Modul funktioniert nur diese Syntax und der 'back'-Befehl (aktuell)
    
    * /fsapi/command_execution : Wenn die PIN bekannt ist, können bestimmte Befehle auf dem Radio ausgeführt werden

    * /scanner/command_scanner : Sucht nach möglichen Befehlen, die bei /fsapi/command_execution verwendet werden können

    * /scanner/firmware_downloader : Versucht die aktuelle Version der Firmware für das Gerät herunterzuladen.

    * /scanner/web_scanner : kombiniert /fsapi/resolve_pin mit /fsapi/command_execution und /scanner/firmware_downloader

## TODO
------------
1. Iperf-Command injection
2. FSH-1 filesystem structure of binary (firmware)





 
    