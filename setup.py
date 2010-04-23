#!/usr/bin/env python
from setuptools import setup, find_packages
import os, re

PKG='txsimplegeo'
VERSIONFILE = os.path.join(PKG, '_version.py')
verstr = "unknown"
try:
    verstrline = open(VERSIONFILE, "rt").read()
except EnvironmentError:
    pass # Okay, there is no version file.
else:
    VSRE = r"^verstr = ['\"]([^'\"]*)['\"]"
    mo = re.search(VSRE, verstrline, re.M)
    if mo:
        verstr = mo.group(1)
    else:
        print "unable to find version in %s" % (VERSIONFILE,)
        raise RuntimeError("if %s.py exists, it must be well-formed" % (VERSIONFILE,))

setup(name=PKG,
      version=verstr,
      description="twisted library for interfacing with SimpleGeo's API",
      author="Wade Simmons",
      author_email="wade@simplegeo.com",
      url="http://github.com/simplegeo/txsimplegeo",
      packages = find_packages(),
      license = "MIT License",
      install_requires=['httplib2>=0.6.0', 'oauth2>=1.1.3', 'simplejson>=2.0.9'],
      keywords="simplegeo",
      zip_safe = False, # We prefer unzipped for easier access to source code.
      tests_require=['coverage'])
