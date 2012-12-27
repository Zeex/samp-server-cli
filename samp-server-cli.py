#!/usr/bin/env python
#
# Copyright (c) 2012 Zeex
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import argparse
import itertools
import os
import random
import string
import subprocess
import sys

def generate_password(size=10, chars=string.ascii_letters + string.digits):
  return ''.join(random.choice(chars) for x in range(size))

def get_options():
  parser = argparse.ArgumentParser(
    description='A command line interface to SA:MP server',
    fromfile_prefix_chars='@',
  )

  parser.add_argument('-a', '--announce', dest='announce', action='store_const', const=1, default=0, help='announce to server masterlist')
  parser.add_argument('-b', '--bind', dest='bind', metavar='address', help='bind to specific IP address')
  parser.add_argument('--chatlogging', dest='chatlogging', action='store_const', const=1, default=0, help='enable chat logging')
  parser.add_argument('-c', '--command', metavar=('cmd', 'args'), nargs='+', help='override server startup command (path to server executable by default)')
  parser.add_argument('-C', '--config', metavar='filename', help='copy options from file')
  parser.add_argument('-e', '--extra', dest='extra', metavar='name value', nargs='+', help='write additional options (order may change)')
  parser.add_argument('-f', '--filterscript', dest='filterscripts', metavar='name/path', action='append', help='add filter script; multiple occurences of this option are allowed')
  parser.add_argument('-g', '-g0', '--gamemode', '--gamemode0', dest='gamemode0', metavar='name/path', required=True, help='set startup game mode (mode #0)')
  for i in range(1, 10):
    parser.add_argument('-g%d' % i, '--gamemode%d' % i, dest='gamemode%d' % i, metavar='name/path', help='set game mode #%d' % i)
  parser.add_argument('-t', '--gamemodetext', dest='gamemodetext', metavar='"My Game Mode"', help='set game mode text (shown in server browser)')
  parser.add_argument('-n', '--hostname', dest='hostname', metavar='"My SA-MP server"', help='set host name (shown in server browser)')
  parser.add_argument('-l', '--lanmode', dest='lanmode', action='store_const', const=1, default=0, help='enable LAN mode')
  parser.add_argument('--logqueries', action='store_const', const=1, default=0, help='enable logging of queries sent by players')
  parser.add_argument('--logtimeformat', metavar='format', help='set log timestamp format')
  parser.add_argument('-m', '--mapname', dest='mapname', metavar='name', help='set map name (shown in server browser)')
  parser.add_argument('--maxplayers', metavar='number', type=int, default=500, help='set max. number of players')
  parser.add_argument('--maxnpc', metavar='number', type=int, default=0, help='set max. number of NPCs (bots)')
  parser.add_argument('-o', '--output', dest='output', action='store_const', const=1, default=0, help='enable console output')
  parser.add_argument('-P', '--password', dest='password', metavar='password', nargs='?', const=generate_password(), help='server password')
  parser.add_argument('-s', '--serverdir', metavar='path', help='set directory of server executable (current directory by default); not necesssary if you use -c')
  parser.add_argument('-d', '--plugin', dest='plugins', metavar='name/path', action='append', help='add plugin; multiple occurences of this option are allowed')
  parser.add_argument('-p', '--port', dest='port', metavar='number', type=int, default=7777, help='set server port')
  parser.add_argument('-q', '--query', dest='query', action='store_const', const=1, default=0, help='allow querying server info from outside world (e.g. server browser)')
  parser.add_argument('-r', '--rcon', dest='rcon', action='store_const', const=1, default=0, help='enable RCON (Remote CONsole) access')
  parser.add_argument('-R', '--rconpassword', dest='rcon_password', metavar='password', default=generate_password(), help='RCON admin password')
  parser.add_argument('-T', '--timestamp', dest='timestamp', action='store_const', const=1, default=0, help='show timestamps in log')
  parser.add_argument('-u', '--weburl', dest='weburl', metavar='url', help='website URL')
  parser.add_argument('-w', '--workingdir', metavar='path', default='.', help='set working directory (current directory by default)')

  args = parser.parse_args(sys.argv[1:])
  return vars(args)

def read_config(filename):
  options = {}
  file = open(filename, 'r')
  for line in file.readlines():
    try:
      name, value = string.split(line.strip(), maxsplit=1)
      options[name] = value
    except ValueError:
      continue
  file.close()
  return options

def write_config(filename, options):
  file = open(filename, 'w')
  for name, value in options.items():
    if value is not None:
      file.write('%s %s\n' % (name, value))
  file.close()

def group(n, iterable, padvalue=None):
    "group(3, 'abcdefg', 'x') --> ('a','b','c'), ('d','e','f'), ('g','x','x')"
    return itertools.izip_longest(*[iter(iterable)]*n, fillvalue=padvalue)

def quiet_mkdir(path):
  if not os.path.exists(path):
    os.mkdir(path)

def run(options):
  working_dir = options['workingdir']
  if not os.path.exists(working_dir):
    os.mkdir(working_dir)
  del options['workingdir']

  server_dir = options['serverdir']
  if server_dir is None:
    server_dir = os.environ.get('SAMP_SERVER_ROOT')
    if server_dir is None:
      server_dir = os.getcwd()
  if not os.path.isabs(server_dir):
    server_dir = os.path.abspath(server_dir)
  del options['serverdir']

  command = options['command']
  if command is None:
    if os.name == 'nt':
      server_exe = 'samp-server.exe'
    else:
      server_exe = 'samp03svr'
    command = os.path.join(server_dir, server_exe)
  del options['command']

  extra = options['extra']
  if extra is not None:
    extra_options = dict(group(2, extra))
    options.update(extra_options)
  del options['extra']

  config = options['config']
  if config is not None:
    config_options = read_config(config)
    options.update(config_options)
  del options['config']

  dirs = { 'filterscripts': 'filterscripts',
           'plugins':       'plugins',
         }
  for i in range(0, 10):
    dirs['gamemode%d' % i] = 'gamemodes'

  for name, dir in dirs.items():
    dir = os.path.join(working_dir, dir)
    values = options[name]
    if values is None:
      continue
    if not type(values) is list:
      values = [values]
    if values is not None:
      for i, v in enumerate(values):
        if not os.path.isabs(v) and not v.startswith('.'):
          # If this is a relative path that does not start with a '.' leave it
          # as is. This is how you typically write script names in server.cfg.
          continue
        else:
          # Otherwise make it relative to the corresponding directory.
          values[i] = os.path.relpath(v, dir)
      options[name] = '%s' % ' '.join(values)

  write_config(os.path.join(working_dir, 'server.cfg'), options)

  quiet_mkdir(os.path.join(working_dir, 'gamemodes'))
  quiet_mkdir(os.path.join(working_dir, 'filterscripts'))

  os.chdir(working_dir)
  try:
    subprocess.call(command)
  except KeyboardInterrupt:
    pass

if __name__ == '__main__':
  run(get_options())
