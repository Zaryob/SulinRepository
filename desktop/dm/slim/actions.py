#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from inary.actionsapi import cmaketools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import get

def setup():
    shelltools.system("sed -i -e 's|#xserver_arguments.*|xserver_arguments   -nolisten tcp vt07|'\
		-e 's|/var/run/slim.lock|/var/lock/slim.lock|' \
		-e 's|halt_cmd.*|halt_cmd            /sbin/poweroff|'\
		-e 's|reboot_cmd.*|reboot_cmd          /sbin/reboot|'\
		-e 's|console_cmd.*|console_cmd         /usr/bin/terminal|'\
		-e 's|login_cmd.*|login_cmd           exec /bin/sh -l /etc/X11/xinit/xinitrc|' \
		-e 's|screenshot_cmd.*|screenshot_cmd      scrot /slim.png|' \
		-e 's|imagemagick|scrot|' \
		-e 's|current_theme.*|current_theme       SulinOS|' \
		slim.conf")
    cmaketools.configure("-DCMAKE_BUILD_TYPE=Release \
			-DCMAKE_SKIP_RPATH=ON \
			-DCMAKE_INSTALL_PREFIX=/usr \
			-DUSE_PAM=yes \
			-DUSE_CONSOLEKIT=no")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    inarytools.removeDir("/lib/")

    inarytools.dodoc("COPYING","TODO", "README", "ChangeLog", "THEMES")
