#!/usr/bin/env python
import setuptools

setuptools.setup(
    name="txeffect",
    version="1.0.0",
    description="Effect/Twisted integration",
    long_description=open("README.rst").read(),
    url="https://github.com/python-effect/txeffect/",
    author="Christopher Armstrong",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    packages=["txeffect"],
    install_requires=["effect", "twisted"],
)
