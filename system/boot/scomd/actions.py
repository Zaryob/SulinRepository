#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import shelltools
from inary.actionsapi import inarytools
from inary.actionsapi import get

def install():
    shelltools.cd("scomd")
    inarytools.dosed("bin/adduser.py", "plugdev", "removable")
    shelltools.system("python3 setup.py install %s" % get.installDIR())

    # in new tarball remove
    shelltools.chmod(get.installDIR() + "/sbin/scomd_cgroupfs.py" , 0o755)

    inarytools.dodir("/etc/scomd/services/enabled")
    inarytools.dodir("/etc/scomd/services/disabled")
    inarytools.dodir("/etc/scomd/services/conditional")
