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

import netius

from . import proxy_r

class DockerProxyServer(proxy_r.ReverseProxyServer):

    def __init__(self, *args, **kwargs):
        proxy_r.ReverseProxyServer.__init__(self, *args, **kwargs)
        linked = netius.conf_suffix("_PORT")
        for name, host in netius.legacy.iteritems(linked):
            base = name[:-5].lower()
            if name.endswith("_ENV_PORT"): continue
            if base[-1].isdigit(): continue
            host = host.replace("tcp://", "http://")
            host = str(host)
            self.hosts[base] = host

if __name__ == "__main__":
    server = DockerProxyServer()
    server.serve(env = True)
