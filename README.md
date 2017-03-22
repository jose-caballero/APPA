# APPA
an Alternative framework for Particle Physics Analysis

===============================================================================
    DEPLOYMENT
===============================================================================

As root:

    $ git clone https://github.com/jose-caballero/APPA.git
    $ cd APPA
    $ python setup.py bdist_rpm
    $ rpm -Uhv dist/appa-<version>.noarch.rpm

As user:

    $ git clone https://github.com/jose-caballero/APPA.git
    $ cd APPA
    $ python setup.py install --home=$HOME
    $ export PYTHONPATH=$HOME/lib/python:$PYTHONPATH

