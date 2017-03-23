#!/usr/bin/env python

import logging
import logging.handlers
import time

from appa.external.pluginmanager import PluginManager

def setlogging(framework):
    
    log = logging.getLogger()
    logStream = logging.StreamHandler()
    # FIXME
    # we may want to change the message format
    FORMAT='%(asctime)s (UTC) [ %(levelname)s ] %(name)s %(filename)s:%(lineno)d %(funcName)s(): %(message)s'
    formatter = logging.Formatter(FORMAT)
    formatter.converter = time.gmtime  # to convert timestamps to UTC
    logStream.setFormatter(formatter)
    loglevel = framework.conf.get("FRAMEWORK", "loglevel")
    if loglevel.lower() == "debug":
        level = logging.DEBUG
    elif loglevel.lower() == "info":
        level = logging.INFO
    else:
        level = logging.WARNING
    log.addHandler(logStream)
    log.setLevel(level)
    return log


def getplugins(framework):

    plugins = []
    for step in framework.analysis:
        plugin = getplugin(framework, step)
        plugins.append(plugin)
    return plugins

def getplugin(framework, step):
    '''
    get the right plugin for each analysis name
    First, we need to find out which type of plugin/name is:
        - selection
        - scale
    then we get that plugin
    '''

    kind = framework.conf.get(step, 'type')
    if kind == 'selection':
        paths = 'appa.plugins.event.selection'
    else:
        paths = 'appa.plugins.event.scale'

    pluginname = framework.conf.get(step, "name")

    # FIXME
    # we are instantiating pm many times 
    pm = PluginManager()
    return pm.getplugin(framework, paths, pluginname, framework.conf, step)
