import os
import sys
from setuptools import setup, find_packages

from monolith.aggregator import __version__


here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.rst')) as f:
    CHANGES = f.read()

PYTHON26 = sys.version_info < (2, 7)

requires = [
    'gevent',
    'oauth2client',
    'elasticsearch',
    'PyMySQL',
    'python-gflags',
    'SQLAlchemy',
    'google-api-python-client',
    'requests',
]


if PYTHON26:
    requires.extend([
        'argparse',
        'simplejson',
    ])

test_requires = requires + [
    'coverage',
    'nose',
    'pyelastictest',
    'Sphinx',
    'unittest2',
    'HTTPretty',
]


setup(name='monolith.aggregator',
      version=__version__,
      description='10allday Monolith Aggregator',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
      ],
      author='10allday Services',
      author_email='services-dev@10allday.com',
      url='https://github.com/10allday-Software/monolith-aggregator',
      license="MPLv2.0",
      packages=find_packages(),
      namespace_packages=['monolith'],
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=test_requires,
      test_suite="monolith.aggregator.tests",
      extras_require={'test': test_requires},
      entry_points="""
      [console_scripts]
      monolith-extract = monolith.aggregator.extract:main
      monolith-ga-oauth = tools.auth_google_analytics:main
      """)
