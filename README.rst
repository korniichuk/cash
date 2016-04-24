.. contents:: Table of contents
   :depth: 2

Installation
============
Install the cash from PyPI
--------------------------
::

    $ sudo pip3 install cash

Install the cash from GitHub
----------------------------
::

    $ sudo pip3 install git+git://github.com/korniichuk/cash#egg=cash

Upgrade the cash from PyPI
--------------------------
::

    $ sudo pip3 install -U cash

or::

    $ sudo pip3 install --upgrade cash

Uninstall the cash
------------------
::

    $ sudo pip3 uninstall cash

Development installation
========================
::

    $ git clone git://github.com/korniichuk/cash.git
    $ cd cash
    $ sudo pip3 install .

User guide
==========
Help
----
The standard output for –help::

    $ cash -h

or::

    $ cash --help

For information on using subcommand "SUBCOMMAND", do::

    $ cash SUBCOMMAND -h

or::

    $ cash SUBCOMMAND --help

Example::

    $ cash init -h

Version
-------
The standard output for –version::

    $ cash -v

or::

    $ cash --version
