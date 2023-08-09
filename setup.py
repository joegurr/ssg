#!/usr/bin/env python3

from setuptools import setup

setup(
    name="ssg",
    version=1.0,
    packages=["ssg"],
    entry_points={"console_scripts": ["ssg = ssg.cli:main"]},
)
