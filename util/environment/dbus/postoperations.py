#!/usr/bin/env python3

import os

OUR_ID = 101
OUR_NAME = "dbus"
OUR_DESC = "dbus"


def postInstall():
    try:
        os.system("groupadd -g %d %s" % (OUR_ID, OUR_NAME))
        os.system("useradd -m -d /var/run/dbus -r -s /bin/false -u %d -g %d %s -c \"%s\"" % (OUR_ID, OUR_ID, OUR_NAME, OUR_DESC))
        os.system("dbus-uuidgen --ensure")
        os.system("ln -sv /var/lib/dbus/machine-id /etc")
        os.system("chown -v root:dbus /usr/libexec/dbus-daemon-launch-helper && chmod -v 4750 /usr/libexec/dbus-daemon-launch-helper")
    except:
        pass

def postRemove():
    try:
        os.system("userdel %s" % OUR_NAME)
        os.system("groupdel %s" % OUR_NAME)
    except:
        pass

def preRemove():
    pass
