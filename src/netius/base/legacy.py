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

__author__ = "João Magalhães joamag@hive.pt>"
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

import sys
import functools

import urllib #@UnusedImport

try: import cStringIO
except: import io; cStringIO = io

try: import urlparse as _urlparse
except: import urllib.parse; _urlparse = urllib.parse

PYTHON_3 = sys.version_info[0] >= 3
""" Global variable that defines if the current python
interpreter is at least python 3 compliant, this is used
to take some of the conversion decision for runtime """

if PYTHON_3: UNICODE = None
else: UNICODE = unicode #@UndefinedVariable

if PYTHON_3: STRINGS = (str,)
else: STRINGS = (str, unicode) #@UndefinedVariable

if PYTHON_3: INTEGERS = (int,)
else: INTEGERS = (int, long) #@UndefinedVariable

def ord(value):
    if PYTHON_3: return value
    return __builtins__.ord(value)

def chr(value):
    if PYTHON_3: return bytes([value])
    return __builtins__.chr(value)

def chri(value):
    if PYTHON_3: return value
    return __builtins__.chr(value)

def bin(value):
    if not PYTHON_3: return value
    if type(value) == bytes: return value
    return value.encode("ascii")

def str(value):
    if not PYTHON_3: return value
    if type(value) == str: return value
    return value.decode("ascii", "ignore")

def to_bytes(value):
    if PYTHON_3: return bytes(value)
    else: return str(value)

def reduce(*args, **kwargs):
    if PYTHON_3: return functools.reduce(*args, **kwargs)
    return reduce(*args, **kwargs)

def urlparse(*args, **kwargs):
    return _urlparse(*args, **kwargs)

def urlencode(*args, **kwargs):
    if PYTHON_3: urllib.parse.urlencode(*args, **kwargs)
    else: return urllib.urlencode(*args, **kwargs) #@UndefinedVariable

def unquote(*args, **kwargs):
    if PYTHON_3: urllib.parse.unquote(*args, **kwargs)
    else: return urllib.unquote(*args, **kwargs) #@UndefinedVariable

def StringIO(*args, **kwargs):
    return cStringIO.StringIO(*args, **kwargs)

def BytesIO(*args, **kwargs):
    if PYTHON_3: return cStringIO.BytesIO(*args, **kwargs)
    else: return cStringIO.StringIO(*args, **kwargs)
