from setuptools import setup

setup(
  name='helloworld',
  version='0.0.1',
  description='Say Hello!',
  py_modules=["helloworld"],
  package_dir={'': 'src'},
  classifiers=["Programming Language :: Python :: 3.0",
               "Programming Language :: Python :: 3.6",
               "Programming Language :: Python :: 3.7",
               "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)"
               "Operating System :: OS Independent"]
)