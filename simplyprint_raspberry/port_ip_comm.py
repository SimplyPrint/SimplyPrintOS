# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, unicode_literals

#
# SimplyPrint
# Copyright (C) 2020-2021  SimplyPrint ApS
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from .base import *
import time
import subprocess
import sys
import threading
from datetime import datetime


def save_port(val):
    if val != config.get("info", "op_proxy_port"):
        set_config_key("info", "op_proxy_port", val)
        set_config()

        from .startup import run_startup
        # Startup can hang for a bit, so run as a thread to avoid issues there
        startup_thread = threading.Thread(target=run_startup)
        startup_thread.start()


def save_ip(val):
    if val != config.get("info", "local_ip"):
        set_config_key("info", "local_ip", val)
        set_config()
