# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

long_description='''Image Morphology Toolbox

The image morphology toolbox implements the basic binary and
greyscale morphology operations, working with numpy arrays
representing

This is a pure Python package which is the companion package
to the book "Hands-on Morphological Image Processing." It has been
updated to work with numpy and the names and interfaces have been
Pythonised.

Includes basic operations such as
    - erode
    - dilate
    - open
    - tophat opening
    - watershed
    - ...

*Website*: `http://luispedro.org/software/pymorph <http://luispedro.org/software/pymorph>`_

Future Plans
~~~~~~~~~~~~

When all functions have a corresponding unit test and the whole of the
API documentation has been re-written into numpy rst format, I will release
version 1.0.

The package is actively maintained and any reported bug will be fixed fast.
'''
classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Scientific/Engineering :: Image Recognition',
    'Topic :: Software Development :: Libraries :: Python Modules',
    ]

setup(name='pymorph',
      version='0.91.7',
      description='Image Morphology Toolbox',
      long_description=long_description,
      author='Luis Pedro Coelho',
      author_email='lpc@cmu.edu',
      url='http://luispedro.org/software/pymorph/',
      license='BSD',
      packages=find_packages(),
      )


