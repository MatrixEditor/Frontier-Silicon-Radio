# MEDION MD87805 (English version)

## Web-FsAPI

In many IoT-devices by the company Frontier-Silicon (now Frontier Smart [FS]) a web-control API is integrated. You can control the device without any authentication by accessing it over the browser. It will send you a XML-Response with the status and optional a value (GET requests).

To run the [main.py](https://github.com/MatrixEditor/Frontier-Silicon-Radio/blob/main/src/main.py) script you have to install the following python libraries: (use py or python)

    python -m pip install beautifulsoup4
and

    python -m pip install requests


## fsapi-Dokumentation

[Here](https://github.com/flammy/fsapi/blob/master/FSAPI.md) an unofficial documentation of (almost) all functions provided by this FsAPI.

## Main-File

After starting the program with the [main.py](https://github.com/MatrixEditor/Frontier-Silicon-Radio/blob/main/src/main.py) file, the following commands can be used:

    * use [module-name] : uses the specified module
    * modules : prints all loaded modules
    * quit : closes the application

When you use a module (for module-details read below) only the following commands can be used:

    * set [option] [value] : sets a new value to the specified option
    * show options : shows all options related to the used module
    * run : runs the module
    * back : returns back to the main/start menu

## Modules

    * /fsapi/resolve_pin : Tries to get the current PIN of the specified FS-device. This module has a unique syntax: run -i <IP> [-d (when you want to print debug info)]. 'set' and 'show options' annot be used.

    * /fsapi/command_execution : executes the specified command on the device and prints its response

    * /scanner/firmware_downloader : tries to download the current firmware-version of the device.

    * /scanner/web_scanner : combines /fsapi/resolve_pin, /fsapi/command_execution and /scanner/firmware_downloader

    * /scanner/command_scanner : scans the device for all known commands in order to get the ones who can be used

You can find a list of commands [here](https://github.com/MatrixEditor/Frontier-Silicon-Radio/blob/main/src/fsradio/base/commands.py).