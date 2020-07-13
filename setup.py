import learntools
from setuptools import setup
from setuptools import find_packages

setup(name='learntools',
      version=learntools.__version__,
      description='Utilities for Python Summer School exercises',
      url='https://github.com/ferdinandb/PSS_Learntools',
      license='Apache 2.0',
      packages=find_packages(),
      zip_safe=True)
