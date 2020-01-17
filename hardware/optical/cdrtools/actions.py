from inary.actionsapi import autotools
from inary.actionsapi import shelltools
from inary.actionsapi import inarytools
from inary.actionsapi import get

shelltools.export("GMAKE_NOWARN","true")

def build():
    autotools.make("-j1 INS_BASE=/usr DEFINSUSR=root DEFINSGRP=root")

def install():
    autotools.rawInstall("DESTDIR={} -j1 INS_BASE=/usr DEFINSUSR=root DEFINSGRP=root".format(get.installDIR()))
    inarytools.removeDir("/usr/share/man/man3")

