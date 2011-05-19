#!/usr/bin/env python
"""
Accept a module's full path on standard in and convert it to
an ImpactJS-compliant module name. This program depends on knowing
the project's top-level directory as a second argument. If this is
blank then this will output just the filename without its extension.

E.G. Given '/Users/joe/src/game/lib/game/entities/thing.js' this will write
out 'game.entities.thing'.

Used in the 'igm' Snippet.
"""

import sys
import os

path = sys.argv[1]
rel_to = sys.argv[2]

# Throw away the extension; we don't care about it.
module_name, extension = os.path.splitext(os.path.relpath(path, rel_to + '/lib'))

# Change the '/' to '.'.
print module_name.replace('/', '.')
