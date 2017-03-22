#!/usr/bin/env python

#######################
#   FAKE PLUGIN
#######################

import logging

class fake(object):
    def __init__(self, framework, name, conf):
        self.name = name
        self.conf = conf
        self.log = logging.getLogger('fake')
        
    def run(self):
        self.log.debug("running fake scale")
