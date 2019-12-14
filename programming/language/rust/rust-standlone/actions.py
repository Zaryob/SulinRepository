from inary.actionsapi import shelltools
from inary.actionsapi import get

NoStrip = "/"
IgnoreAutodep = True

def install():
    shelltools.system("./install.sh --destdir={0}/ --prefix={0}/usr \
                                    --sysconfdir={0}/etc --bindir={0}/usr/bin \
                                    --libdir={0}/usr/lib --datadir={0}/usr/share \
                                    --mandir={0}/usr/share/man \
                                    --docdir={0}/usr/share/doc/ \
                                    --disable-ldconfig".format(get.installDIR()))
