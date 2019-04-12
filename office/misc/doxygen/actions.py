# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get
from inary.actionsapi import cmaketools

def setup():
    # --shared and --release are default parameters, however we just write them
    # to down to avoid confusing wheter it's a static/shared or release/debug
    # package at the first look :)
    cmaketools.configure()
    
def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    #inarytools.doman("doc/doxywizard.1")

    # The makefile included is there to generate the html files
    # The user itself should execute it
    inarytools.insinto(get.docDIR() + "/doxygen" , "examples")

    inarytools.dodoc("LANGUAGE.HOWTO", "LICENSE", "README*", "VERSION")
