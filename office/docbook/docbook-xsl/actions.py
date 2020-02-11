
#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def install():
    autotools.rawInstall("DESTDIR=%s/usr/share/xml/docbook/xsl-stylesheets"
                         % get.installDIR())
    inarytools.insinto("/usr/share/xml/docbook/xsl-stylesheets/","VERSION.xsl")


    inarytools.dodoc("AUTHORS", "BUGS", "COPYING", "NEWS", "README",
                    "RELEASE-NOTES.txt", "TODO", "VERSION")
