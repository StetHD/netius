#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Netius System
# Copyright (c) 2008-2016 Hive Solutions Lda.
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

__copyright__ = "Copyright (c) 2008-2016 Hive Solutions Lda."
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
        address = kwargs.get("address", None)
        if not address: return False
        import netius.common
        address = address[0]
        return netius.common.assert_ip4(
            address,
            allowed,
            default = False
        )

    def auth_i(self, *args, **kwargs):
        return self.__class__.auth(
            allowed = self.allowed,
            *args,
            **kwargs
        )
