# MEDION MD87805

Ich habe mich mal intensiver mit diesem Internet-Radio beschäftigt, um Lücken im System zu finden, die es möglich machen, die Kontrolle über dieses Radio zu übernehmen. Wichtig dabei ist, dass jede Anfrage und Antwort bei dem Radio unverschlüsselt (als plain-text!!) über das Netzwerk versandt wird.

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



 
    