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

from appa.external.pluginmanager import PluginManager


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
        param1 = <value>
        param2 = <value>
        ...

        [A_n]
        type = <selection|scale>
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
        self.loglevel = self.conf.get('FRAMEWORK', 'loglevel')
        self._setlogging(self)       
        self.plugins = self._getplugins()

        # run
        self.run()


    # -------------------------------------------------------------------------
    # preparing everything 
    # -------------------------------------------------------------------------

    def _setlogging(self):
        
        self.log = logging.getLogger()
        logStream = logging.StreamHandler()
        # FIXME
        # we may want to change the message format
        FORMAT='%(asctime)s (UTC) [ %(levelname)s ] %(name)s %(filename)s:%(lineno)d %(funcName)s(): %(message)s'
        formatter = logging.Formatter(FORMAT)
        formatter.converter = time.gmtime  # to convert timestamps to UTC
        logStream.setFormatter(formatter)
        if self.loglevel == "debug":
            level = logging.DEBUG
        elif self.loglevel == "info":
            level = logging.INFO
        else:
            level = logging.WARNING
        logStream.setLevel(level)
        self.log.addHandler(logStream)


    def _getplugins(self):

        plugins = []
        for step in self.analysis:
            plugin = self._getplugin(step)
            plugins.append(plugin)
        return plugins

    def _getplugin(self, name):
        '''
        get the right plugin for each analysis name
        First, we need to find out which type of plugin/name is:
            - selection
            - scale
        then we get that plugin
        '''
        kind = self.conf.get(name, 'type')
        if kind == 'selection':
            paths = 'appa.plugins.event.selection'
        else:
            paths = 'appa.plugins.event.scale'
            
        return PluginManager.getplugin(self, paths, name, self.conf)


    # -------------------------------------------------------------------------
    # run 
    # -------------------------------------------------------------------------

    def run(self):
        '''
        runs, in order, all steps included in the analysis input option
        '''

        for plugin in self.plugins:
            plugin.run() 
