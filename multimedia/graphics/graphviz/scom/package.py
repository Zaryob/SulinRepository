#!/usr/bin/env python3

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    # write layout's config
    os.system("/usr/bin/dot -c")
