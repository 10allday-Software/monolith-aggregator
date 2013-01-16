import os
from setuptools import setup, find_packages
from aggregator import __version__


here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst')) as f:
    README = f.read()

requires = ['SQLAlchemy', ]
test_requires = requires + ['unittest2', 'nose', 'coverage']

setup(name='monolith-aggregator',
      version=__version__,
      description='The monolith aggregator',
      long_description=README,
      classifiers=[
        "Programming Language :: Python",
        ],
      classifiers=[
          "Programming Language :: Python",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
      ],
      author='Mozilla Services',
      author_email='services-dev@mozilla.org',
      url='https://github.com/mozilla/monolith-aggregator',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires + ['unittest2',],
      test_suite="aggregator",
      entry_points="""
      [console_scripts]
      monolith-extract = aggregator.extract:main
      """)
