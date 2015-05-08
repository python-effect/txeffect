#!/usr/bin/env python
import setuptools

setuptools.setup(
    name="txeffect",
    version="0.1a1",
    description="Effect/Twisted integration",
    long_description=open('README.rst').read(),
    url="http://github.com/radix/txeffect/",
    author="Christopher Armstrong",
    license="MIT",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        ],
    packages=['effect'],
    install_requires=['effect', 'twisted', 'six', 'characteristic>=14.0.0'],
    )