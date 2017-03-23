#!/usr/bin/env python

#######################
#   FAKE PLUGIN
#######################

import logging

class fakeselection(object):
    def __init__(self, framework, conf, section):
        self.section = section
        self.conf = conf
        self.log = logging.getLogger('fakeselection')
        self.param1 = self.conf.get(section, "param1")
        
    def run(self):
        self.log.debug("running fake selection")
        self.log.debug("param1 = %s" %self.param1)
