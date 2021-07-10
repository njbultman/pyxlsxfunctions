#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 19:49:56 2021

@author: nickbultman
"""

from setuptools import setup, find_packages

setup(
      author = 'Nick Bultman',
      description = 'Use Excel functions in Python',
      name = 'pyxlsxfunctions',
      version = '0.2.0',
      install_requires = ['datetime', 'numpy', 'pandas'],
      packages = find_packages(include = ['pyxlsxfunctions', 'pyxlsxfunctions.*']),
      classifiers = [
              'Development Status :: 2 - Pre-Alpha',
              'Intended Audience :: Developers',
              'License :: OSI Approved :: MIT License',
              'Natural Language :: English',
              'Programming Language :: Python :: 3.7',
              ]
)