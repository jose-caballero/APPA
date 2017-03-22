#!/usr/bin/env python

#######################
#   FAKE PLUGIN
#######################

import logging

class fakescale(object):
    def __init__(self, framework, name, conf):
        self.name = name
        self.conf = conf
        self.log = logging.getLogger('fakescale')
        self.param1 = self.conf.get(name, 'param1')
        
    def run(self):
        self.log.debug("running fake scale")
        self.log.debug("param1 = %s" %self.param1)
