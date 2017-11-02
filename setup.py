#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name="zmop",
      version="0.1.0",
      description="zmop Python SDK",
      license="BSD",
      install_requires=["requests"],
      author="zhima",
      url="https://github.com/gusibi/zmop",
      download_url="https://github.com/gusibi/zmop/archive/master.zip",
      packages=find_packages(),
      keywords=["python", "zmop", "sdk"],
      zip_safe=True)
