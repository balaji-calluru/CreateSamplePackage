from setuptools import setup

with open("README.md") as fh:
    long_description = fh.read()

setup(
  name='helloworld',
  version='0.0.1',
  description='Say Hello!',
  py_modules=["helloworld"],
  package_dir={'': 'src'},
  classifiers=["Programming Language :: Python :: 3.0",
               "Programming Language :: Python :: 3.6",
               "Programming Language :: Python :: 3.7",
               "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
               "Operating System :: OS Independent"],
  long_description=long_description,
  long_description_content_type="text/markdown",
  install_requires = [
      "blessings ~= 1.7",
  ],
  extras_require = {
      "dev":[
          "pytest>=3.7",
      ],
  },
  url="https://github.com/balaji-calluru/CreateSamplePackage",
  author="Balaji Calluru",
  author_email="balaji.calluru@gmail.com",
)
