import logging
import logging.handlers
import traceback

from pprint import pprint


class NullHandler(logging.Handler):
    """
    This handler does nothing. It's intended to be used to avoid the
    "No handlers could be found for logger XXX" one-off warning. This is
    important for library code, which may contain code to log events. If a user
    of the library does not configure logging, the one-off warning might be
    produced; to avoid this, the library developer simply needs to instantiate
    a NullHandler and add it to the top-level logger of the library module or
    package.
    """
    def handle(self, record):
        pass

    def emit(self, record):
        pass

    def createLock(self):
        self.lock = None



class PluginManager(object):
    '''
    Entry point for plugins creation, initialization, starting, and configuration. 
    '''
    def __init__(self):
        '''
        Top-level object to provide plugins. 
        '''
        self.log = logging.getLogger('pluginsmanager')
        self.log.addHandler(NullHandler())
        self.log.debug('PluginManager initialized.')


    def getpluginlist(self, parent, paths, namelist, *k, **kw):
        '''
        Provides a list of initialized plugin objects. 
        parent: reference to the calling object
        paths: list of subdirectories from where to import the plugin(s)
        namelist: list of plugins to be imported
        #config: config parser object to feed to the plugin
        #section: the section name in the config object that is relevant for this plugin
        '''
        plist = []
        for name in namelist:
            po = self._getplugin(parent, paths, name, *k, **kw)
            plist.append(po)
        self.log.info('returning a list of plugins = %s' %plist)
        return plist


    def getplugin(self, parent, paths, name, *k, **kw):
        '''
        Provides a single initialized plugin object. 
        parent: reference to the calling object
        paths: list of subdirectories from where to import the plugin(s)
        name: name of the single plugin to be imported
        #config: config parser object to feed to the plugin
        #section: the section name in the config object that is relevant for this plugin
        '''
        p = self._getplugin(parent, paths, name, *k, **kw)
        self.log.info('returning a plugin = %s' %p)
        return p


    def _getplugin(self, parent, paths, name, *k, **kw):
        """
        returns an initialized plugin object.
        parent: reference to the calling object
        paths: list of subdirectories from where to import the plugin(s)
        name: name of the single plugin to be imported
        #config: config parser object to feed to the plugin
        #section: the section name in the config object that is relevant for this plugin
        """
        self.log.debug('Starting')
        ko = self._getpluginclass(paths, name)
        po = ko(parent, *k, **kw)
        self.log.debug('Leaving, returning %s' %po)
        return po
    
        
    def _getpluginclass(self, paths, name):
        '''
        returns a plugin class. 
        The __init__() methods have not been called yet.
        paths: list of subdirectories from where to import the plugin(s)
        name: name of the single plugin to be imported
        '''
        self.log.debug('Starting')
       
        if type(paths) is list: 
            ppath = '.'.join(paths)
        else:
            ppath = paths
        ppath = ppath + '.' + name
        
        try:
            plugin_module = __import__(ppath, globals(), locals(), name)
        except Exception, ex:
            self.log.error(ex)
    
        plugin_class = getattr(plugin_module, name)
        self.log.debug("Retrieved plugin with class name %s" % name)
        return plugin_class
    

