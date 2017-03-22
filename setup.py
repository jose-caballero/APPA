#!/usr/bin/env python
#
# Setup prog for APPA
#
#

import commands
import os
import re
import sys

from appa import infoservice
release_version=infoservice.__version__

from distutils.core import setup
from distutils.command.install import install as install_org
from distutils.command.install_data import install_data as install_data_org


# ===========================================================
#                D A T A     F I L E S 
# ===========================================================

libexec_files = ['libexec/%s' %file for file in os.listdir('libexec') if os.path.isfile('libexec/%s' %file)]
systemd_files = [ 'etc/appa', ]
etc_files = ['etc/appa.conf', ]

# -----------------------------------------------------------

rpm_data_files=[('/usr/libexec', libexec_files),
                ('/etc/appa', etc_files),
                #('/usr/share/doc/appa', docs_files),                                        
               ]


home_data_files=[('etc', libexec_files),
                 ('etc', etc_files),
                ]

# -----------------------------------------------------------

def choose_data_files():
    rpminstall = True
    userinstall = False
     
    if 'bdist_rpm' in sys.argv:
        rpminstall = True

    elif 'install' in sys.argv:
        for a in sys.argv:
            if a.lower().startswith('--home'):
                rpminstall = False
                userinstall = True
                
    if rpminstall:
        return rpm_data_files
    elif userinstall:
        return home_data_files
    else:
        # Something probably went wrong, so punt
        return rpm_data_files
       
# ===========================================================

# setup for distutils
setup(
    name="APPA",
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
    
    data_files = choose_data_files()
)
