---
layout: default
title: "Kernel unter Debian kompilieren"
lang: de
license: ['CC BY-NC-SA 2.0', 'http://creativecommons.org/licenses/by-nc-sa/2.0/de/']
---

*__Achtung__: Dieser Artikel ist aus dem Jahr 2004 und wurde zuletzt im Jahr 2008
bearbeitet. Möglicherweise hat sich einiges geändert. Hinweise bitte per E-Mail.*

 * [Kernel unter Debian kompilieren](#kernel_unter_debian_kompilieren)
 * [make-kpkg installieren](#makekpkg_installieren)
 * [Den Kernel-Source vorbereiten](#den_kernelsource_vorbereiten)
 * [Kernel bauen](#kernel_bauen)
 * [Kernel installieren](#kernel_installieren)
 * [Zusammenfassung](#zusammenfassung)

Kernel unter Debian kompilieren
===============================

Der Linuxkernel lässt sich unter Debian GNU/Linux natürlich genau wie in anderen Distributionen mit `make menuconfig && make dep && make bzImage && make modules` erstellen und anschließend die erstellten Binärdaten in `/boot` und ``/lib/modules/`uname -r`/`` kopieren. Dies läuft aber dem sauberen Paket-Management (dpkg) unter Debian zuwieder und erhöht den Aufwand für die Sysadmins. Aus diesem Grunde gibt es das Programm make-kpkg.

make-kpkg installieren
======================

make-kpkg ist ein Teil des Paketes kernel-package und ist demnach einfach über: "`apt-get install kernel-package`" zu installieren. Wie wir später sehen werden ist auch das Paket fakeroot nützlich weshalb wir noch ein "`apt-get install fakeroot`" dranhängen. Natürlich brauchen wir auch die Quelltexte des Linux-Kernels, den wir zu kompilieren wünschen. Dieser ist entweder direkt bei kernel.org oder die entsprechenden Source-Pakete bei Debian z.b. kernel-source-2.4.20 zu erhalten. Um make menuconfig verwenden zu können wird noch die libncurses aus dem Paket libncurses-dev benötigt, die wir bei Bedarf installieren müssen. Weitere zwingend benötigte Pakete sind libc-dev, gcc, debianutils und make die, sollten sie noch nicht vorhanden sein, nachinstalliert werden.

Den Kernel-Source vorbereiten
=============================

Wir haben uns im vorhergehenden Schritt die Kernel-Quellen besorgt. Wir gehen davon aus, das diese in /usr/src/ liegen. Wir entpacken diese wie gewohnt - "`tar xvjf kernel-source-2.4.20.tar.bz2`" tut das hervorragend - und verlinken das Ergebnis mit /usr/src/linux indem wir ein "`ln -sf kernel-source-2.4.20 linux`" absetzen.
Idealerweise führen wir alle Operationen, die keine root-Rechte benötigen als Benutzer aus, welcher der Gruppe "src" angehört. Außer für die "`apt-get install`" benötigen wir die Rechte bis jetzt nicht. 
Nun kann der Kernel konfiguriert werden also: "`cd linux" und "make-kpkg --config=menuconfig --revision=Custom.1.00 configure`"

Kernel bauen
============

Nachdem die Vorbereitungen abgeschlossen sind und eine Kernel-Configuration vorliegt, kann mit dem Kompiliervorgang begonnen werden.
In unserem Beispiel: "`make-kpkg --rootcmd=fakeroot kernel_image`".
Wenn wir auch das dazugehörige initrd-image bauen wollen so wird der Parameter --initrd benötigt:
"`make-kpkg --initrd --rootcmd=fakeroot kernel_image`".
Das erzeugt, wenn alles glatt läuft - ein .deb file in /usr/src/. Der Revisions-Parameter sollte natürlich den eigenen Bedürfnissen angepasst werden. Sollte der Vorgang im aktuellen Verzeichnis wiederholt werden, ist es wichtig zuerst "make-kpkg clean" durchzuführen um alte Daten aus dem Weg zu räumen. Außer dem Parameter --revision kann man sinnigerweise noch eine Extraversion anhängen; dies geschieht mit --append_to_version (nur Kleinbuchstaben, -, + und .). Diese Extraversion ist mit dem uname -a sichtbar und hat somit auch Auswirkungen auf das Modul-Ladeverhalten.

Kernel installieren
===================

Installieren läßt sich das deb-file (als root) mit "`dpkg -i kernel-image-2.4.20_Custom.1.00_i386.deb`". Dabei wird der Kernel nach /boot und die Module in ein passendes Verzeichnis kopiert. Das kernel-image wird automatisch mit /vmlinuz verlinkt, was bei Debian der Standard-Eintrag in der Bootmanager-Konfiguration (z.B. lilo oder grub) sein sollte. Der Ursprüngliche Standardkernel wird mit /vmlinuz.old verlinkt und bleibt also funktional. Dies gilt aber nur bei anderen Kernel-Versionen oder Extra-Versionen! Neue Revisionen werden überschrieben!
Das Kernel-Debian-Paket kann nun einfach kopiert werden auch auf anderen Rechnern sein Unheil anrichten.

Zusammenfassung
===============

Für die Eiligen:

    sudo apt-get install make gcc kernel-package fakeroot libncurses-dev kernel-source-2.4.20
    cd /usr/src/
    tar xvjf kernel-source-2.4.20.tar.bz2
    ln -sf kernel-source-2.4.20 linux
    cd linux
    make-kpkg clean
    make-kpkg --config=menuconfig --revision=1.00.Custom configure
    make-kpkg --initrd --rootcmd=fakeroot kernel_image
    cd ..
    sudo dpkg -i kernel-image-2.4.20_Custom.1.00_i386.deb

