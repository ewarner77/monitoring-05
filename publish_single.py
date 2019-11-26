#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2014 Roger Light <roger@atchoo.org>
#
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Eclipse Distribution License v1.0
# which accompanies this distribution.
#
# The Eclipse Distribution License is available at
#   http://www.eclipse.org/org/documents/edl-v10.php.
#
# Contributors:
#    Roger Light - initial implementation

# This shows an example of using the publish.single helper function.

import context  # Ensures paho is in PYTHONPATH
import paho.mqtt.publish as publish
auth = { 'username' : "ewarner77", 'password' : "my74bbug" }
publish.single("shop/cnc03/running", "0" , hostname="167.71.147.221", auth=auth)
