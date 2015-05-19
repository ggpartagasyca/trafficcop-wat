try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'WAT',
    'author': 'Andrew Philpot',
    'url': 'http://www.isi.edu',
    'download_url': 'http://www.isi.edu',
    'author_email': 'philpot@isi.edu',
    'version': '0.1',
    'install_requires': ['nose'],
    # these are the subdirs of the current directory that we care about
    'packages': ['wat'],
    'scripts': [],
    'name': 'trafficop-wat'
}

setup(**config)
