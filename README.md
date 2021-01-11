# Hello World

This is a tutorial to create python packages from scratch and publish to PyPI

Based on the video Tutorial by Mark Smith (@judy2k)

## https://www.youtube.com/watch?v=GIF3LaRqgXo


## Creating a new package

Create helloworld.py

Create setup.py

Then run setup

Example setup command:

```
python.exe setup.py bdist_wheel
```

## Installing project

Install the package in the local directory

Example pip command:

```
pip install -e .[dev]
```

## How to Perfect it

Add the getignore see http://gitignore.io

Get the license from https://choosealicense.com/

Get the classifiers from https://pypi.org/classifiers

## Usage

```python
from helloworld import say_hello

# Generate "Hello, World!"
say_hello()

# Generate "Hello, Everybody!"
say_hello("Everybody")
```
## Test with pytest

Install pytest
Add pytest to the setup.py and execute the pip again

Create test_helloworld.py

Execute pytest
```
pytest
```

## Source Distribution

```
python setup.py sdist
```

## Create Manifest

```
pip install check-manifest
check-manifest --create
git add MANIFEST.in
```

## Prepare for "Publishing"

```
python setup.py bdist_wheel sdist
```

## Install Twine to Publish

```
pip install twine
twine upload dist/*
```

## (Productionize) Install tox

```
pip install tox
```

## Other stuff to do -- Cookiecutter

```
pip install cookiecutter
cookiecutter gh:ionelmc/cookiecutter-pylibrary
```

## More Info

https://github.com/judy2k/publishing_python_packages_talk
