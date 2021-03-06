'''
simple script for direct submission of python scripts to torque
'''

import os

if 'PBS_O_WORKDIR' in os.environ:
    os.chdir(os.environ['PBS_O_WORKDIR'])

    #use a non-X requiring background
    import matplotlib
    matplotlib.use('Agg')

if 'PBS_DEBUG' in os.environ:
    from printlocalsetup import *

from torque import *

#end
