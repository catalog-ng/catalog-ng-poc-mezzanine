## Open Data Catalog (odcatalog)
## Mezzanine-powered data catalog management application
##--------------------------------------------------------------------

import sys
from pkg_resources import normalize_path
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

version = '0.1'

install_requires = [
    "mezzanine",
    "south",
]

setup(
    name='mezzanine-odcatalog',
    version=version,
    packages=find_packages(),
    url='',
    license='Apache License, Version 2.0',
    author='Samuele Santi',
    author_email='samuele@samuelesanti.com',
    description='Simple Open Data catalog management application',
    long_description='Simple Open Data catalog management application',
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 2.7",
    ],
    package_data={'': ['README.rst', 'LICENSE']},
)
