# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import pythonmodules

def build():
    pythonmodules.compile(pyVer='3')

def install():
    pythonmodules.install("--install-lib=/usr/lib/sulin",pyVer='3')
    inarytools.dodir("/usr/bin/")
    shelltools.system("install inary-cli {}/usr/bin/inary-cli".format(get.installDIR()))

    inarytools.dosym("inary-cli", "/usr/bin/inary")

    inarytools.dodir("/var/lib/inary/info/")

    inarytools.dodir("/usr/lib/sulin")
