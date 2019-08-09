#!/usr/bin/env python3

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/usr/sbin/alternatives \
               --install /usr/lib32/libGL.so.1.2.0 libGL-32bit /usr/lib32/mesa/libGL.so.1.2.0 80 \
               --slave /usr/lib32/xorg/modules/volatile xorg-modules-volatile-32bit /var/empty")

    if not os.path.lexists("/usr/lib32/libGL.so.1"):
        os.symlink("libGL.so.1.2.0", "/usr/lib32/libGL.so.1")

def preRemove():
    # FIXME This is not needed when upgrading package; but inary does not
    #       provide a way to learn operation type.
    #os.system("/usr/sbin/alternatives --remove libGL-32bit /usr/lib32/mesa/libGL.so.1.2")
    pass
