from inary.actionsapi import autotools
from inary.actionsapi import get

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR={}".format(get.installDIR()))
