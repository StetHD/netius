#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Netius System
# Copyright (C) 2008-2012 Hive Solutions Lda.
#
# This file is part of Hive Netius System.
#
# Hive Netius System is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Hive Netius System is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Hive Netius System. If not, see <http://www.gnu.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2012 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "GNU General Public License (GPL), Version 3"
""" The license for the module """

import os
import glob
import setuptools

setuptools.setup(
    name = "netius",
    version = "0.9.45",
    author = "Hive Solutions Lda.",
    author_email = "development@hive.pt",
    description = "Netius System",
    license = "GNU General Public License (GPL), Version 3",
    keywords = "netius net infrastructure",
    url = "http://netius.com",
    zip_safe = False,
    packages = [
        "netius",
        "netius.adapters",
        "netius.auth",
        "netius.base",
        "netius.clients",
        "netius.common",
        "netius.extra",
        "netius.servers",
        "netius.sh"
    ],
    package_dir = {
        "" : os.path.normpath("src")
    },
    package_data = {
        "netius" : ["base/extras/*", "servers/extras/*"]
    },
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7"
    ]
)
