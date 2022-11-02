#!/usr/bin/env python

# mraptor3 is a stub that redirects to mraptor.py, for backwards compatibility

import sys, os, warnings

warnings.warn('mraptor3 is deprecated, mraptor should be used instead.', DeprecationWarning)

# IMPORTANT: it should be possible to run oletools directly as scripts
# in any directory without installing them with pip or setup.py.
# In that case, relative imports are NOT usable.
# And to enable Python 2+3 compatibility, we need to use absolute imports,
# so we add the oletools parent folder to sys.path (absolute+normalized path):
_thismodule_dir = os.path.normpath(os.path.abspath(os.path.dirname(__file__)))
_parent_dir = os.path.normpath(os.path.join(_thismodule_dir, '..'))
if _parent_dir not in sys.path:
    sys.path.insert(0, _parent_dir)

from olltools.mraptor import *
from olltools.mraptor import __doc__, __version__

if __name__ == '__main__':
    main()
