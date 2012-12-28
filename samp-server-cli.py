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
import platform
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

  argument = lambda *args, **kwargs: parser.add_argument(*args, **kwargs)

  argument('-a', '--announce', dest='announce', action='store_const', const=1, default=0, help='announce to server masterlist')
  argument('-b', '--bind', dest='bind', metavar='address', help='bind to specific IP address')
  argument('--chatlogging', dest='chatlogging', action='store_const', const=1, default=0, help='enable chat logging')
  argument('-c', '--command', dest='command', metavar=('cmd', 'args'), nargs='+', help='override server startup command (path to server executable by default)')
  argument('-C', '--config', dest='config', metavar='filename', help='copy options from file')
  argument('-D', '--debug', dest='debug', nargs=argparse.REMAINDER, help='run under debugger')
  argument('-e', '--extra', dest='extra', metavar='name value', nargs='+', help='write additional options (order may change)')
  argument('-f', '--filterscript', dest='filterscripts', metavar='name/path', action='append', help='add filter script; multiple occurences of this option are allowed')
  argument('-g', '-g0', '--gamemode', '--gamemode0', dest='gamemode0', metavar='name/path', required=True, help='set startup game mode (mode #0)')
  for i in range(1, 10):
    argument('-g%d' % i, '--gamemode%d' % i, dest='gamemode%d' % i, metavar='name/path', help='set game mode #%d' % i)
  argument('-t', '--gamemodetext', dest='gamemodetext', metavar='"My Game Mode"', help='set game mode text (shown in server browser)')
  argument('-n', '--hostname', dest='hostname', metavar='"My SA-MP server"', help='set host name (shown in server browser)')
  argument('-l', '--lanmode', dest='lanmode', action='store_const', const=1, default=0, help='enable LAN mode')
  argument('-L', '--local', dest='local', action='store_true', default=False, help='run in current directory (same as if you pass "--workdir .")')
  argument('--logqueries', dest='logqueries', action='store_const', const=1, default=0, help='enable logging of queries sent by players')
  argument('--logtimeformat', dest='logtimeformat', metavar='format', help='set log timestamp format')
  argument('-m', '--mapname', dest='mapname', metavar='name', help='set map name (shown in server browser)')
  argument('--maxplayers', dest='maxplayers', metavar='number', type=int, default=500, help='set max. number of players')
  argument('--maxnpc', dest='maxnpc', metavar='number', type=int, default=0, help='set max. number of NPCs (bots)')
  argument('-o', '--output', dest='output', action='store_const', const=1, default=0, help='enable console output')
  argument('-P', '--password', dest='password', metavar='password', nargs='?', const=generate_password(), help='server password')
  argument('-s', '--servdir', dest='servdir', metavar='path', help='set directory of server executable (current directory by default); not necesssary if you use -c')
  argument('-d', '--plugin', dest='plugins', metavar='name/path', action='append', help='add plugin; multiple occurences of this option are allowed')
  argument('-p', '--port', dest='port', metavar='number', type=int, default=7777, help='set server port')
  argument('-q', '--query', dest='query', action='store_const', const=1, default=0, help='allow querying server info from outside world (e.g. server browser)')
  argument('-r', '--rcon', dest='rcon', action='store_const', const=1, default=0, help='enable RCON (Remote CONsole) access')
  argument('-R', '--rconpassword', dest='rcon_password', metavar='password', default=generate_password(), help='RCON admin password')
  argument('-T', '--timestamp', dest='timestamp', action='store_const', const=1, default=0, help='show timestamps in log')
  argument('-u', '--weburl', dest='weburl', metavar='url', help='website URL')
  argument('-w', '--workdir', dest='workdir', metavar='path', help='set working directory (server directory by default)')

  args = parser.parse_args(sys.argv[1:])
  return vars(args)

def quiet_mkdir(path):
  if not os.path.exists(path):
    os.mkdir(path)

def is_windows():
  system = platform.system()
  return system == 'Windows' or system.startswith('CYGWIN_NT')

def is_linux():
  system = platform.system()
  return system == 'Linux'

def read_config(filename):
  options = {}
  with open(filename, 'r') as file:
    for line in file.readlines():
      try:
        name, value = string.split(line.strip(), maxsplit=1)
        options[name] = value
      except ValueError:
        continue
  return options

def write_config(filename, options):
  with open(filename, 'w') as file:
    for name, value in options.items():
      if value is not None:
        file.write('%s %s\n' % (name, value))

def group(n, iterable, padvalue=None):
    "group(3, 'abcdefg', 'x') --> ('a','b','c'), ('d','e','f'), ('g','x','x')"
    return itertools.izip_longest(*[iter(iterable)]*n, fillvalue=padvalue)

def run(options):
  servdir = options['servdir']
  if servdir is None:
    servdir = os.environ.get('SAMP_SERVER_ROOT')
    if servdir is None:
      servdir = os.getcwd()
  if not os.path.isabs(servdir):
    servdir = os.path.abspath(servdir)
  del options['servdir']

  local = options['local']
  del options['local']

  workdir = options['workdir']
  if local:
    workdir = os.getcwd()
  else:
    if workdir is None:
      workdir = servdir
    else:
      quiet_mkdir(workdir)
  del options['workdir']

  command = options['command']
  if command is None:
    if is_windows():
      exe = 'samp-server.exe'
    else:
      exe = 'samp03svr'
    command = os.path.join(servdir, exe)
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

  plugins = options['plugins'] 
  if plugins is not None:
    if is_windows():
      ext = '.dll'
    else:
      ext = '.so'
    for i, p in enumerate(plugins):
      if not p.lower().endswith(ext):
        plugins[i] += ext

  dirs = { 'filterscripts': 'filterscripts',
           'plugins':       'plugins',
         }
  for i in range(0, 10):
    dirs['gamemode%d' % i] = 'gamemodes'

  for name, dir in dirs.items():
    dir = os.path.join(workdir, dir)
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

  debug = options['debug']
  if debug is not None:
    command = ['gdb'] + debug + ['--args'] + command
  del options['debug']

  write_config(os.path.join(workdir, 'server.cfg'), options)

  quiet_mkdir(os.path.join(workdir, 'gamemodes'))
  quiet_mkdir(os.path.join(workdir, 'filterscripts'))

  os.chdir(workdir)
  try:
    return subprocess.call(command)
  except KeyboardInterrupt:
    return 0

if __name__ == '__main__':
  sys.exit(run(get_options()))
