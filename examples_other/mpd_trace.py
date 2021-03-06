#!/usr/bin/env python
#
# Author: Mike McKerns (mmckerns @caltech and @uqfoundation)
# Copyright (c) 1997-2016 California Institute of Technology.
# Copyright (c) 2016-2017 The Uncertainty Quantification Foundation.
# License: 3-clause BSD.  The full license text is available at:
#  - https://github.com/uqfoundation/pyina/blob/master/LICENSE
"""
run three basic tests of the MPI installation
"""

import subprocess
CPI = "~/src/mpich-1.0.7/examples/cpi"

command = 'mpdtrace'
print "\nlaunch: %s" % command
subprocess.call(command, shell=True)

command = 'mpdringtest 10'
print "\nlaunch: %s" % command
subprocess.call(command, shell=True)

command = 'mpiexec -n 4 hostname'
print "\nlaunch: %s" % command
subprocess.call(command, shell=True)

#command = 'mpiexec -n 1 %s' % CPI
#print "\nlaunch: %s" % command
#subprocess.call(command, shell=True)

# End of file
