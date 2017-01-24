try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'simNMR',
    'author': 'Arturas Grauslys',
    'url': 'http://github.com/ArturasG',
    'download_url': 'http://github.com/ArturasG/simNMR',
    'author_email': 'agraulsys@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['simNMR'],
    'scripts': [],
    'name': 'simNMR'
}

setup(**config)
