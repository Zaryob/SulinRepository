# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import shelltools
from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import get


def install():
    for i in {"/bin", "/sbin", "/lib", "/lib32","/data/srv","/kernel"
              "/etc","/tmp","/data/misc","/data/mnt"
              "/data","/data/user","/data/app","/data/app/system","/data/user/root",
              "/tmp", "/var/tmp", "/var/lock", "/usr", "/usr/bin",
              "/usr/lib", "/usr/lib32", "/usr/libexec", "/usr/share",
              "/run","/run/shm","/run/media","/lib/modules","lib/firmware",
              "/usr/local", "/usr/local/bin", "/usr/local/lib", "/usr/local/libexec",
              "/usr/local/lib32"}:
        inarytools.dodir(i)

    autotools.rawInstall("DESTDIR={}".format(get.installDIR()))

# Adjust permissions
    shelltools.chmod("{}/tmp".format(get.installDIR()), 0o1777)
    shelltools.chmod("{}/var/tmp".format(get.installDIR()), 0o1777)
    shelltools.chmod("{}/run/shm".format(get.installDIR()), 0o1777)
    shelltools.chmod("{}/var/lock".format(get.installDIR()), 0o775)
    shelltools.chmod("{}/usr/share/baselayout/shadow".format(get.installDIR()), 0o600)

# SulinOS GNU/Linux filesystem architecture (like android and LFS)
#
#    /data/
#        ->app          = Userspace application directory
#            ->system   = Userspace optional system application ( /opt linked here )
#        ->data         = Infinitive loop directory ( /data linked here )
#        ->media        = userspace mounted volumes ( linked /var/run/media )
#        ->mnt          = Root mounted volumes ( /mnt linked here )
#        ->user         = User's home directory ( /home linked here )
#            ->root     = The root home ( /root linked here )
#        ->misc         = Is an unused directory
#        ->tmp          = Temp directory ( linked /tmp )
#        ->srv          = Served directory ( /srv linked here )
#
#    /kernel/
#         ->boot        = Linux kernel files ( /boot linked here )
#         ->modules     = Linux kernel module files ( /lib/modules linked here )
#         ->firmware    = Linux kernel firmware files ( /lib/firmware linked here )
#         ->dev         = The dev directory ( /dev linked here )
#         ->sys         = The sys directory ( /sys linked here )
#         ->proc        = The proc directory ( /proc linked here )
#
#    /run => /var/run
#

    inarytools.dosym("../run", "/var/run")
    inarytools.dosym("data/user", "/home")
    inarytools.dosym("../run/media", "/data/media")
    inarytools.dosym("data/user/root", "/root")
    inarytools.dosym("../tmp/", "/data/tmp")
    inarytools.dosym("../data", "/data/data")
    inarytools.dosym("data/srv", "/srv")
    inarytools.dosym("data/app/system/", "/opt")
    inarytools.dosym("data/mnt/", "/mnt")

    inarytools.dosym("../dev", "/kernel/dev")
    inarytools.dosym("../sys", "/kernel/sys")
    inarytools.dosym("../proc", "/kernel/proc")
    inarytools.dosym("../boot", "/kernel/boot")
    inarytools.dosym("../lib/modules", "/kernel/modules")
    inarytools.dosym("../lib/firmware", "/kernel/firmware")

    if get.ARCH() == "x86_64":
        # Directories for 32bit libraries
        inarytools.dodir("/lib32")
        inarytools.dodir("/usr/lib32")

        # Hack for binary blobs built on multi-lib systems
        inarytools.dosym("../lib", "{}/lib64".format(get.installDIR()))
        inarytools.dosym("../lib", "{}/usr/lib64".format(get.installDIR()))
        inarytools.dosym("../lib", "{}/usr/local/lib64".format(get.installDIR()))

