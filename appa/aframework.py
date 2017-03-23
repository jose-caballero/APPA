#!/usr/bin/env python

__author__ = "Jose Caballero, Oscar Gonzalez"
__copyright__ = "2017 Jose Caballero, Oscar Gonzalez"
__credits__ = []
__license__ = "GPL"
__version__ = "0.9.0"
__maintainer__ = "Jose Caballero, Oscar Gonzalez"
__email__ = "jcaballero.hep@gmail.com, oscar.gonzalez@cern.ch"
__status__ = "Production"


import logging
import logging.handlers
import time

import appa.utils as utils


class Framework(object):
    """
    This is just a first [fake] implementation, mostly to learn.
    Versions 1.x.y and higher will not look anything alike to this.

    Input of the Framework is a ConfigParser object, 
    with all needed info inside.
    This ConfigParser object can be created from multiple sources:
        - a config file
        - a combination of CLI input options
        - data from a DB
        - information from an external framework
        - ...
    However, the source of the info contained in the ConfigParser object
    is not relevant once it gets into this class.

    The format of the ConfigParser content is:

        [FRAMEWORK]
        loglevel = <logging level>
        inputs = <list of input files>
        outputs = <output file>
        analysis = <list of plugins to perform the analysis>

        [A_1]
        type = <selection|scale>
        name = <name of the plugin>
        param1 = <value>
        param2 = <value>
        ...

        [A_n]
        type = <selection|scale>
        name = <name of the plugin>
        param1 = <value>
        param2 = <value>
        ...
        
    """

    def __init__(self, conf):

        self.conf = conf
        self.inputs = self.conf.get('FRAMEWORK', 'inputs')
        self.outputs = self.conf.get('FRAMEWORK', 'outputs')
        analysis = self.conf.get('FRAMEWORK', 'analysis')
        self.analysis = [i.strip() for i in analysis.split(',')]

        # preparing everything 
        self.log = utils.setlogging(self)       
        self.plugins = utils.getplugins(self)

        # run
        self.run()

    # -------------------------------------------------------------------------
    # run 
    # -------------------------------------------------------------------------

    def run(self):
        '''
        runs, in order, all steps included in the analysis input option
        '''

        for plugin in self.plugins:
            plugin.run() 
