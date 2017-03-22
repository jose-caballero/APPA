#!/usr/bin/env python
#
# Setup prog for APPA
#
#

import commands
import os
import re
import sys

from appa import aframework
release_version=aframework.__version__

from distutils.core import setup
from distutils.command.install import install as install_org
from distutils.command.install_data import install_data as install_data_org

# ===========================================================

# setup for distutils
setup(
    name="appa",
    version=release_version,
    description='APPA package',
    long_description='''This package contains the package APPA''',
    license='GPL',
    author='jcaballero, oglez',
    author_email='EMAIL',
    maintainer='MAINTAINER',
    maintainer_email='MEMAIL',
    url='https://github.com/jose-caballero/APPA',
    packages=['appa',
              'appa.external',
              'appa.plugins',
              'appa.plugins.event',
              'appa.plugins.event.selection',
              'appa.plugins.event.scale',

              ],
    scripts = [ # Utilities and main script
               'bin/appa',
              ],
    
    data_files = []
)
