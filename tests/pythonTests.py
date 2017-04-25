#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# This Modularity Testing Framework helps you to write tests for modules
# Copyright (C) 2017 Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# he Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Authors: Tomas Orsava <torsava@redhat.com>
#

from moduleframework import module_framework
import os
from avocado.utils import service

class pythonTests(module_framework.AvocadoTest):
    """
    :avocado: enable
    """
    def testPython(self):
        self.start()

        self.assertIn("Python 3", self.run("python3 --version", shell=True).stdout)
        self.assertEquals("3", self.run("python3 -c \"import sys; print(sys.version[0], end='')\"", shell=True).stdout)

        self.assertIn("SyntaxError: Missing parentheses in call to 'print'",
                self.run("python3 -c \"print 'Is this Python 2?'\"", shell=True, ignore_status=True).stderr)

        # Python regression test suite
        #  - Some tests disabled as they are not expected to pass:
        #    - test_distutils - due to missing gcc
        #    - test_shutil, test_socket, test_pty
        #  - If there is a problem, this test should fail due to the return value,
        #    the assertNotIn() is there just for safety.
        self.assertNotIn("tests failed:",
                self.run("python3 -m test -x test_distutils -x test_shutil -x test_socket -x test_pty", shell=True).stdout)

        # Add more tests when The Python module is built and we know what packages it contains
