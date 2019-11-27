#!/path/to/python3
'''
    Author:  Ricky Martinez
    Purpose: Simple module created to provide verification based on the username of the person logged in.
             Permissions can be set here:
                ``` /path/to/auth_users.ini ```
'''
import datetime
import sys
import os

# TODO: REMOVE
from pprint import pprint

AUTH_FILE = "/path/to/auth_users.ini"

auth_users = {}
with open(AUTH_FILE, 'r') as f:
    lines = f.readlines()
    for line in lines:
        if line.startswith('#') or line[0] == '\n':
            continue;
        user, envs = line.split(maxsplit=1);
        auth_users[user] = envs.strip().split(',');

def getUser():
    return os.environ['REMOTE_USER']

def checkUser(user, env):
    if user in auth_users and env in auth_users[user]:
        return True
    else:
        return False

