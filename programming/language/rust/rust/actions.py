from inary.actionsapi import shelltools
from inary.actionsapi import inarytools
from inary.actionsapi import get

NoStrip = "/"
IgnoreAutodep = True

def build():
    shelltools.system("CARGO_HOME={0} RUSTUP_HOME={0} bash ./rustup-init.sh -y --profile complete --no-modify-path -v".format(get.installDIR()))

def install():
    inarytools.cd(get.installDIR())
    shelltools.system("rm -rf downloads tmp update-hashes env settings.toml bin")
    shelltools.system("mkdir usr/ ; mv toolchains/*/* usr/ ; rm -rf toolchains")
    shelltools.system("mv usr/etc etc")
