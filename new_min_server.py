# coding=utf-8
# !/usr/bin/env python3

"""
    This file is a ported version of the C example bundled with NEAT.
    Note that the NEAT bindings currently require Python 2.7 or larger.
    Python 3 will not work.
"""

import sys
from endpoint import *
from preconnection import *


if __name__ == "__main__":

    local_specifier = LocalEndpoint()
    local_specifier.with_port(5000)
    precon = Preconnection(local_endpoint=local_specifier, transport_properties=None)
    precon.listen()
    sys.exit()