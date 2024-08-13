#!/usr/bin/env python3

import os
import subprocess

# Clone the repository
subprocess.run(
    ['git', 'clone', 'https://github.com/siryle/ansible_homelab.git'])
os.chdir('ansible_homelab')

# Read user input
username = input("Enter username: ")
password = input("Enter password: ")
server_ip = input("Enter server IP address: ")

# Replace values in vars.yml file
with open('group_vars/all/vars.yml', 'r') as f:
    content = f.read()
content = content.replace('<username>', username)
content = content.replace('<server_ip>', server_ip)
content = content.replace('<password>', password)
with open('group_vars/all/vars.yml', 'w') as f:
    f.write(content)

# Replace values in inventory file
with open('inventory', 'r') as f:
    content = f.read()
content = content.replace('<server_ip>', server_ip)
content = content.replace('<username>', username)
content = content.replace('<password>', password)
with open('inventory', 'w') as f:
    f.write(content)

# Run the playbook
# subprocess.run(['ansible-playbook', 'main.yml'])
