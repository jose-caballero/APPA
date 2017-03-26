an Alternative framework for Particle Physics Analysis

---
Deployment
---

**As root**:

    $ git clone https://github.com/jose-caballero/APPA.git
    $ cd APPA
    $ python setup.py bdist_rpm
    $ rpm -Uhv dist/appa-<version>.noarch.rpm

**As user:**

    $ git clone https://github.com/jose-caballero/APPA.git
    $ cd APPA
    $ python setup.py install --home=$HOME
    $ export PYTHONPATH=$HOME/lib/python:$PYTHONPATH


---
Testing 
---

1) install it
2) create a fake config file like this:

        [FRAMEWORK]
        loglevel = debug
        inputs = in
        outputs = out
        analysis = fakeselection, fakescale

        [fakeselection]
        name = fakeselection
        type = selection
        param1 = value1      

        [fakescale]
        name = fakescale
        type = scale 
        param1 = value1      

Note two fake plugins -fakeselection and fakescale- are provided

3) run script /usr/bin/appa (or $HOME/bin/appa) passing as input the location of the config file

---
