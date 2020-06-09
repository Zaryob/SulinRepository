#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import pythonmodules


def install():
    inarytools.insinto("/usr/bin/", "xterm_colour_chart.py")
    shelltools.chmod(get.installDIR() + "/usr/bin/xterm_colour_chart.py", mode=0o755)
    inarytools.dosym("/usr/bin/xterm_colour_chart.py", "/usr/bin/xtermcolourchart")
