#!/usr/bin/env python3

import os

def postInstall():
    os.system('groupadd apache')
    os.system('useradd -c "Apache Server" -d /srv/www -g apache -s /bin/false apache')
