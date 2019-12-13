#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import get
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools
from inary.actionsapi import perlmodules

KeepSpecial=["perl"]

def setup():
    # use system zlib
    shelltools.unlinkDir("cpan/Compress-Raw-Zlib/zlib-src")
    inarytools.dosed("MANIFEST", "zlib-src", deleteLine=True)
    inarytools.dosed("cpan/Compress-Raw-Zlib/config.in", "(BUILD_ZLIB\s+=\s)True", r"\1False")
    inarytools.dosed("cpan/Compress-Raw-Zlib/config.in", "(INCLUDE\s+=\s)\.\/zlib-src", r"\1/usr/include")
    inarytools.dosed("cpan/Compress-Raw-Zlib/config.in", "(LIB\s+=\s)\.\/zlib-src", r"\1/usr/lib")

    shelltools.export("LC_ALL", "C")

    #fix one of tests
    #shelltools.system('sed -i "s#version vutil.c .*#version vutil.c f1c7e4778fcf78c04141f562b80183b91cbbf6c9#" t/porting/customized.dat')

    shelltools.system('sh Configure -des \
                      -Darchname=%s-linux \
                      -Dcccdlflags=-fPIC \
                      -Dusedevel \
                      -Dccdlflags="-rdynamic -Wl,--enable-new-dtags" \
                      -Dcc=%s \
                      -Dprefix=/usr \
                      -Dvendorprefix=/usr \
                      -Dsiteprefix=/usr \
                      -Ulocincpth=  \
                      -Doptimize="%s" \
                      -Duselargefiles \
                      -Dusethreads \
                      -Duseithreads \
                      -Dd_semctl_semun \
                      -Dscriptdir=/usr/bin \
                      -Dman1dir=/usr/share/man/man1 \
                      -Dman3dir=/usr/share/man/man3 \
                      -Dinstallman1dir=%s/usr/share/man/man1 \
                      -Dinstallman3dir=%s/usr/share/man/man3 \
                      -Dlibperl=libperl.so.%s \
                      -Duseshrplib \
                      -Dman1ext=1 \
                      -Dman3ext=3pm \
                      -Dcf_by="Sulin" \
                      -Ud_csh \
                      -Di_ndbm \
                      -Di_gdbm \
                      -Di_db \
                      -Ubincompat5005 \
                      -Uversiononly \
                      -Dpager="/usr/bin/less -isr" \
                      -Dd_gethostent_r_proto -Ud_endhostent_r_proto -Ud_sethostent_r_proto \
                      -Ud_endprotoent_r_proto -Ud_setprotoent_r_proto \
                      -Ud_endservent_r_proto -Ud_setservent_r_proto \
                      -Dlibpth="/lib /usr/lib" \
                      ' %(get.ARCH(), get.CC(), get.CFLAGS(), get.installDIR(), get.installDIR(), get.srcVERSION()))


def build():
    # colorgcc uses Term::ANSIColor
    paths = get.ENV("PATH").split(":")
    if "/usr/share/colorgcc" in paths:
        paths.remove("/usr/share/colorgcc")
    shelltools.export("PATH", ":".join(paths))
    ##
    autotools.make()

#def check():
#    autotools.make("-j1 test_harness")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.remove("/usr/bin/perl")
    # Conflicts with perl-Module-Build
    # inarytools.remove("/usr/bin/config_data")

    inarytools.dosym("/usr/bin/perl%s" % get.srcVERSION(), "/usr/bin/perl")

    # Perl5 library
    # NEEDS MODIFICATION FOR NEW VERSION
    inarytools.dosym("/usr/lib/perl5/%s/%s-linux-thread-multi/CORE/libperl.so.%s" % (get.srcVERSION(), get.ARCH(), get.srcVERSION()), "/usr/lib/libperl.so")
    inarytools.dosym("/usr/lib/perl5/%s/%s-linux-thread-multi/CORE/libperl.so.%s" % (get.srcVERSION(), get.ARCH(), get.srcVERSION()), "/usr/lib/libperl.so.5")
    inarytools.dosym("/usr/lib/perl5/%s/%s-linux-thread-multi/CORE/libperl.so.%s" % (get.srcVERSION(), get.ARCH(), get.srcVERSION()), "/usr/lib/libperl.so.5.26")
    inarytools.dosym("/usr/lib/perl5/%s/%s-linux-thread-multi/CORE/libperl.so.%s" % (get.srcVERSION(), get.ARCH(), get.srcVERSION()), "/usr/lib/libperl.so.5.26.1")

    # Docs
    inarytools.dodir("/usr/share/doc/%s/html" % get.srcNAME())
    shelltools.system('LD_LIBRARY_PATH=%s ./perl installhtml \
                       --podroot="." \
                       --podpath="lib:ext:pod:vms" \
                       --recurse \
                       --htmldir="%s/usr/share/doc/%s/html"' % (get.curDIR(), get.installDIR(), get.srcNAME()))

    perlmodules.removePodfiles()
    perlmodules.removePacklist()
    inarytools.dodoc("Changes*", "Artistic", "Copying", "README", "AUTHORS")
