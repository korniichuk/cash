# -*- coding: utf-8 -*-

from os.path import dirname, join
from setuptools import setup

setup(
    author="Ruslan Korniichuk",
    author_email="ruslan.korniichuk@gmail.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "License :: Public Domain",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Office/Business",
        "Topic :: Office/Business :: Financial",
        "Topic :: Utilities"
    ],
    description="The personal finance utility",
    download_url="https://github.com/korniichuk/rich/archive/0.1.zip",
    entry_points={'console_scripts': 'rich=rich.rich:main'},
    include_package_data=True,
    install_requires=[
        "configobj",
        "matplotlib"
    ],
    keywords=["finance", "python3", "rich"],
    license="Public Domain",
    long_description=open(join(dirname(__file__), "README.rst")).read(),
    name="rich",
    packages=["rich"],
    platforms=["Linux"],
    url="https://github.com/korniichuk/rich/",
    version="0.1a1",
    zip_safe=True
)
