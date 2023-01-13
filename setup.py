#!/usr/bin/env python3

from setuptools import setup

setup(
    name="eps",
    version="1.0",
    author="lwzm",
    url="https://github.com/lwzm/eps",
    py_modules=["eps"],
    classifiers=[
        "Environment :: Console",
        "Programming Language :: Python :: 3",
    ],
)

# $ ./setup.py sdist bdist_wheel
# $ twine upload dist/fsmhub-xxx
