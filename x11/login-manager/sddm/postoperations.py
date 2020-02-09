#!/usr/bin/env python3

import os, re
import shutil

OUR_ID = 65
OUR_NAME = "sddm"
OUR_DESC = "sddm"

DATADIR = "/var/lib/sddm"
DATADIRMODE = 0755

def postInstall():

    # On first install...
    if not os.path.exists(DATADIR):
        os.makedirs(DATADIR, DATADIRMODE)

    try:
        os.system ("groupadd -g {} {}".format(OUR_ID, OUR_NAME))
        os.system ("useradd -m -d /var/lib/sddm -r -s /bin/false -u {} -g {} {} -c {}".format(OUR_ID, OUR_ID, OUR_NAME, OUR_DESC))
        os.system ("passwd -l sddm > /dev/null")
        os.system("/bin/chown -R sddm:sddm {}".format(DATADIR))
    except:
        pass
        

def postRemove():
    try:
        os.system ("userdel " + OUR_NAME)
        os.system ("groupdel " + OUR_NAME)
    except:
        pass





