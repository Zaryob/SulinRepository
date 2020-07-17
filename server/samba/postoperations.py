#/usr/bin/python

import os

def postInstall():
    if not os.path.exists("/data/user/samba"):
        os.system("/bin/mkdir /data/user/samba")
        os.system("/bin/chmod 0777 /data/user/samba")

    # needed by non-root sharing support.
    os.system("/bin/mkdir /var/lib/samba/usershares")
    os.system("/bin/chgrp users /var/lib/samba/usershares")
    os.system("/bin/chmod 1777 /var/lib/samba/usershares")

    os.system("/bin/chmod 0750 /var/lib/samba/winbindd_privileged")
