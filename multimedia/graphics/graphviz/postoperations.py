#!/usr/bin/env python3

import os

def postInstall():
    # write layout's config
    os.system("/usr/bin/dot -c")
