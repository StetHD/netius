#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Netius System
# Copyright (c) 2008-2017 Hive Solutions Lda.
#
# This file is part of Hive Netius System.
#
# Hive Netius System is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by the Apache
# Foundation, either version 2.0 of the License, or (at your option) any
# later version.
#
# Hive Netius System is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License for more details.
#
# You should have received a copy of the Apache License along with
# Hive Netius System. If not, see <http://www.apache.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2017 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

from . import base

class AddressAuth(base.Auth):

    def __init__(self, allowed = [], *args, **kwargs):
        base.Auth.__init__(self, *args, **kwargs)
        self.allowed = allowed

    @classmethod
    def auth(cls, allowed = [], *args, **kwargs):
        import netius.common
        host = kwargs.get("host", None)
        headers = kwargs.get("headers", {})
        if not host and not headers: return False
        address = headers.get("X-Forwarded-For", host)
        address = headers.get("X-Client-IP", address)
        address = headers.get("X-Real-IP", address)
        address = address.split(",", 1)[0].strip()
        return netius.common.assert_ip4(
            address,
            allowed,
            default = False
        )

    @classmethod
    def is_simple(cls):
        return True

    def auth_i(self, *args, **kwargs):
        return self.__class__.auth(
            allowed = self.allowed,
            *args,
            **kwargs
        )
