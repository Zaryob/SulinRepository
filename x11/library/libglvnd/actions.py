#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Lime GNU/Linux 2017
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import inarytools
from inary.actionsapi import get, mesontools



def setup():
    mesontools.meson_configure("-D gles1=false")
    
def build():
    mesontools.ninja_build()

def install():
    mesontools.ninja_install()
<<<<<<< HEAD
    #fix conflict with mesa
=======
>>>>>>> c4661ac3fd3f8dcd698f7197e727be09f9a5ec72
