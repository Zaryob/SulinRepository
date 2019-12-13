#!/usr/bin/env python3

import os


def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("rc-update add opentmpfiles-dev default")
    os.system("rc-update add opentmpfiles-setup default")
