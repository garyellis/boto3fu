from boto3fu import __version__
from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name='boto3fu',
    version=__version__,
    descriiption='Boto3 shifu',
    author='Gary Ellis',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['boto3fu = boto3fu.cli:cli']
    },
    install_requires=[
      'boto3',
      'click',
      'pyyaml',
      'tabulate'
    ]
)
