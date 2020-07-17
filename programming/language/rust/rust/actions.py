from inary.actionsapi import shelltools
from inary.actionsapi import inarytools
from inary.actionsapi import get

NoStrip = "/"
IgnoreAutodep = True

def build():
    rustdir=get.pkgDIR()+"/rust-root/"
    options="CARGO_HOME={0} RUSTUP_HOME={0} bash ./rustup-init.sh -y --no-modify-path -v".format(rustdir if get.buildTYPE()!="emul32" else rustdir+"/emul32")
    if get.buildTYPE()=="emul32":
        options+=" --profile minimal --default-host=i686-unknown-linux-gnu"
    else:
        options+=" --profile complete --default-host=x86_64-unknown-linux-gnu"
    shelltools.system(options)

def install():
    rustdir=get.pkgDIR()+"/rust-root/"

    if get.buildTYPE()=="emul32":
        inarytools.cd(rustdir+"/emul32")
        shelltools.system("mkdir -p {}/usr/{{lib,lib32}}/".format(get.installDIR()))
        shelltools.system("cp -Rpvf toolchains/stable-i686-unknown-linux-gnu/lib/rustlib {}/usr/lib/".format(get.installDIR()))
        shelltools.system("cp -Rpvf toolchains/stable-i686-unknown-linux-gnu/lib/*.so* {}/usr/lib32/".format(get.installDIR()))
        return

    inarytools.cd(rustdir)
    shelltools.system("mkdir {0}/usr/ ; cp -Rpvf toolchains/*/* {0}/usr/".format(get.installDIR()))
    inarytools.cd(get.installDIR())
    shelltools.system("mv usr/etc etc")
