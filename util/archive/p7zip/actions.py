#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import shelltools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get

WorkDir = "p7zip_%s" % get.srcVERSION()


def build():
    autotools.make('all3')

def install():
    autotools.install('DEST_DIR="{0}" DEST_HOME="/usr" \
		DEST_MAN="/usr/share/man" \
		DEST_SHARE_DOC="/usr/share/doc/p7zip"'.format(get.installDIR()))
