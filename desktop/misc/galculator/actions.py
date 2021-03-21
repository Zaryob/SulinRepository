#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt
from inary.actionsapi import inarytools
from inary.actionsapi import autotools
from inary.actionsapi import get
import os
#more information : https://gitlab.com/sulinos/inary/tree/master/inary/actionsapi
os.environ["CFLAGS"]+=" -fcommon"
def setup():
    autotools.autogen()
    autotools.configure("")
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

