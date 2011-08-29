---
layout: default
title: Grundlagen was passiert beim "surfen"
license: '<a href="http://creativecommons.org/licenses/by-nc-sa/2.0/de/">CC BY-NC-SA 2.0</a>'
---

  *__Achtung:__ Dieser Artikel ist semantisch nicht in jedem Punkt korrekt.
  Bei Gelegenheit wird er überarbeitet. Die Grundlagen stimmen jedoch.
  Für die angedachte Zielgruppe des Artikels ist dies wohl nicht relevant.*

Grundlagen: Was passiert beim "surfen"?
=======================================

Es handelt sich hier nicht um eine Darstellung bis ins letze Detail. Sie ist für den interessierten Laien gedacht, der einen Überblick über die Funktionsweise des Internets erhalten soll.
Das Internet ist ein Kommunikationsmedium mit verschiedensten Diensten und Kanälen. Einer davon, den wohl neben der E-Mail am meisten genutzen - das World-Wide-Web (www) dient hier als Beispiel. 

Es handelt sich hierbei um eine Arbeitsversion. Anregungen und Korrekturen nehme ich sehr gerne via E-Mail oder Seitenkommentar entgegen.

Die Adresse
===========

Zuerst einmal schauen wir uns die Adressleiste des Browsers an:

**http**://www.toke.de/artikel/grundlagen/was-passiert-beim-surfen/
Der Webbrowser zerlegt diese Zeichenkette in ihre logischen Bestandteile: http Definiert das Protokoll - hier http (HyperText Transmission Protocol) andere übliche Protokolle sind https - hierbei wird der Datenverkehr verschlüsselt übertragen und ftp. Das Protokoll gibt an wie sich der Rechner des surfenden Benutzers (Client) und der des Anbieters der Seite (Server) "unterhalten". Für den Anwender ist es im Endeffekt egal wie die Daten übertragen werden - Hauptsache sie kommen an. Interessant ist es jedoch wieder wenn https verwendet wird hierbei wird der Datenverkehr verschlüsselt, ein Mitlesen anderer ist nahezu ausgeschlossen. Gerade beim Online-Banking und Einkauf ist dies Wichtig! Um https verwenden zu können muß sowohl der Server als auch der Browser des Benutzers dies unterstützen - dies ist auf Serverseite leider viel zu selten der Fall.

http://**www.toke.de**/artikel/grundlagen/was-passiert-beim-surfen/
Hierbei handelt es sich um den sogenannten **Domainnamen**. Dieser ist eine menschenlesbare Adresse des Servers, den man zu erreichen wünscht. Oft ist es so, dass sich unter vielen verschiedenen Adressen ein und derselbe Rechner meldet, so ist in diesem Fall www.thomas.kerpe.net und thomas.kerpe.info derselbe Rechner und führt zur selben Startseite. Eine Genauere Betrachtung von Domainnamen findet man unter Domainnamen.

http://www.toke.de**/artikel/grundlagen/was-passiert-beim-surfen/**
Der **Pfad und Dateiname** der aufzurufenden Seite oder Datei. Sollte diese nicht im Hauptverzeichnis (ROOT-Verzeichnis) liegen befinden sich vor dem Dateinamen noch die Pfad-Angaben z.B. http://www.toke.de/artikel/grundlagen/was-passiert-beim-surfen/. Zu Beachten gilt, dass es sich bei den Trennzeichen zwischen den Rechner, Pfad und Dateiangaben um einen einfachen "Slash" also Schrägstrich (/) handelt. Unter Windows ist der Trenner der Pfadangaben ein sog. "Backslash" also ein umgekehrter Schrägstrich (\). Sollte dieser versehentlich eingegeben werden führt das im Großteil der Fälle zu einer unauffindbaren Seite.
Da es sich bei einem Großteil der Internet-Server nicht um Windows sondern um Unix-Syteme handelt gelten einige Regeln, die man von Windows kennt nicht - andere kommen dazu. So ist zum Beispiel beim Großteil der eingesetzten Systeme so, daß Sie zwischen Groß und Kleinschreibung unterscheiden. "Artikel/Grundlagen/was-passiert-beim-Surfen/" und "artikel/grundlagen/was-passiert-beim-surfen/" sind also verschiedene Adressen!

Domainnamen
===========

Das **Domain Name System (DNS)** ist ein Dienst im Internet, der dafür sorgt, dem Anwender die Möglichkeit zu geben Domainnamen einzugeben. Geschieht dies muss der Computer zuerst den eingegebenen Namen in eine IP-Adresse auflösen. Wie bereits erwähnt werden im Internet Domainnamen eingesetzt um dem Anwender die Arbeit zu erleichtern, denn ein Domainname wird vom Computer in eine IP-Adresse umgewandelt. Dies macht die Anwendersoftware automatisch.

Der Domainname ist hirarchisch aufgebaut und durch "." Punkte (Englisch "dot") getrennt. Der Computer liest den Domainnamen rückwärts - fängt also in unserem Beispiel bei "net" an. Es handelt sich hierbei um die **Toplevel-Domain (TLD)** also der gröbsten Adresszuordnung. Es gibt eine Vielzahl dieser Topleveldomains - so besitzt jedes annerkannte Land eine. Für allgemeingültige Domains - also Domains die keinem Land zugeordnet werden gibt es sogenannte "Generische TLD's" wie "net", "com", "org".
Eine komplette Liste aller Länderdomains findet man bei der verwaltenden Stelle IANA.

Der 2. Teil des eingegeben Namens ist der eigentliche **Domainname**. Er gehört einer Person oder einer Gesellschaft. Und wird bei einer Registratur (für "de" ist das die DENIC eG) eingetragen. Einzeleinträge nimmt die DENIC normalerweise nicht vor - aus diesem Grunde werden Domainnamen von Webhostern bei der DENIC angemeldet. Der Besitzer der Domain muss aber der Endkunde sein!
Zu jeder Domain wird in einer öffentlichen Datenbank (WHOIS) der Kontaktdatenbestand des Domainbesitzers und des Betreibers gespeichert. Jeder kann also den Inhaber einer Domain ermitteln. Fast jede Registratur hat eine eigene Datenbank. Abfragen von "de"-Domains kann man über ein Webformular der DENIC durchführen.

Die folgenden Einträge oft "www" werden **Subdomain** oder **Hostname** genannt. Ich schreibe "Einträge" weil dies auch sehr tief verzweigt sein kann. So ist "www-ibt.etec.uni-karlsruhe.de" ein gültiger Domainname. Korrekt gesprochen ist "www-ibt" der Host oder auch Rechnername, "etec" die Subdomain, "uni-karlsruhe" der Domainname und "de" die Top-Level-Domain

Wir wissen nun, wie ein Domainname aufgebaut ist. Der Computer zerlegt in also in seine Bestandteile und kann nun - vereinfacht ausgedrückt - eine Anfrage bei den Domainservern - eine Art Adressbuch - durchführen. 
Sollte die Domain so wie sie eingegeben ist in den Datenbeständen verfügbar sein, so gibt der Domainserver dem Anwenderprogramm eine sog. IP-Adresse zurück unter der der gewünschte Server erreichbar ist.
Wenn also kein genau passender Eintrag in den Domainservern hinterlegt ist, kann die gewünschte Seite nicht aufgerufen werden. Meist verweisen mehrere Domaineinträge auf die selben Adressen. Es kann also schon ein Unterschied sein, ob man "www.thomas.kerpe.net" oder "thomas.kerpe.net" eingibt.
Ermitteln der IP-Adresse

Die Namensauflösung kann man manuell durchführen: ein Terminal/Shell aufmachen und dann folgendes eingeben: "nslookup www.toke.de". Sie erhalten nun die IP-Adresse des Servers.

IP-Adressen
===========

Wie im Kapitel "Domainnamen" genauer beschrieben wird ein großer Aufwand getrieben um die vom Benutzer eingegebenen Adressen in IP-Adressen umzuwandeln. IP-Adressen sind eindeutige numerische Kennungen von Computern. Sowohl der Rechner, den Sie zu erreichen wünschen, als auch der eigene haben eine solche Adresse. Sie ist zwingend notwendig um eine Kommunikation im Internet zwischen zwei Rechnern zu ermöglichen.

Eine IP-Adresse besteht in der üblichen Schreibweise aus 4 durch Punkte getrennte Zahlenblöcken zwischen 0 und 255. So ist 207.46.249.27 zum Beispiel eine IP-Adresse die zu dem Domainnamen www.microsoft.com gehört.

Datenübertragung mit HTTP
=========================

Nachdem Sie eine Adresse in den Webbrowser eingegeben haben, wird er die IP-Addresse ermitteln und im Anschluß eine Netzwerkverbindung zu besagter Adresse aufbauen.
Sollte dies funktionieren wird der Webserver das angeforderte Dokument an den Anfragenden schicken. Im Fehlerfalle wird eine entsprechende Seite angezeigt. Meist enthaltern diese Fehlerseiten einen standardisierten Fehlercode.
Der Webbrowser weiss nun im Idealfall, was er mit den empfangenen Daten zu tun hat. Entweder er zeigt sie an - zum Beispiel Bilder oder Dokumente - oder er fragt wo er sie Speichern soll.

HTTP-Status-Codes
==================

Eine Liste der üblichsten **Status**- und **Fehlercodes** wie sie im HTTP-Standard festgelegt sind.
Dies ist nicht zu verwechseln mit Fehlern, die von Programmen auf der Serverseite erzeugt wurden!

Die Fehler - oder auch Statuscodes sind in der Regel dreistellige Zahlen. Diese sind standardisiert und nach "Schwere". Definiert sind:

* **1xx** - kein Fehler - Informationen für den Browser - wird nicht angezeigt
* **2xx** - kein Fehler - Erfolgsmeldungen - Jede erfolgreich aufgerufene Seite erzeugt eine 2xx Meldung
* **3xx** - kein Fehler - Umleitungen - kann möglicherweise dem Benutzer angezeigt werden
* **4xx** - Clientfehler - Diese Art von Fehlern sind durch den Client entstanden z.B. eine Ungültige Anfrage gesendet.
* **5xx** - Serverfehler - Hier hat der Server einen Fehler ausgelöst.

"Häufige Fehler"
================

Im folgenden sind einige häufiger angezeigte Fehlercodes mit Erklärung aufgeführt

**300 Multiple Choices** (Status)
Es wurden mehrere Dokumente gefunden, die zu ihrer Anfrage passten - zum Beispiel liegt das Dokument in mehreren Sprachen vor. (Recht selten)

**400 Bad Request** (Fehler)
Ihr Webbrowser hat eine Anfrage an den Webserver geschickt, die dieser nicht versteht. Normalerweise können Sie dies nicht beheben.

**403 Forbidden** (Fehler)
Es handelt sich hierbei entweder um eine fehlgeschlagene Benutzerautentifikation (Passwortabfrage) oder der Seitenbetreiber hat den gewünschten Bereich nicht freigegeben.

**404 Not Found**
Der wohl häufigste Fehler. Hierbei handelt es sich schlicht um eine nichtexistente Datei oder ein Verzeichnis. Eventuell haben Sie sich bei der Adresseingabe vertippt oder die Adresse hat sich geändert.

**500 Internal Server Error**
Hier hat der Server selbst einen Fehler verursacht - zum Beispiel durch ein Serverseitiges Programm - und kann ihre Anfrage nicht beantworten

Es gibt noch eine ganze Reihe weiterer Fehler und Statuscodes, jedoch sollte der Benutzer diese seltener oder nie zu Gesicht bekommen.

Eine Vollständige Liste der spezifizierten Status Codes kann im [RFC 2616](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html) nachgelesen werden.
