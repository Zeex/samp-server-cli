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

  parser.add_argument('-a', '--announce', dest='announce', action='store_const', const=1, default=0, help='toggle announcement to masterlist')
  parser.add_argument('-b', '--bind', dest='bind', metavar='address', help='bind to specific IP address')
  parser.add_argument('-C', '--chatlogging', dest='chatlogging', action='store_const', const=1, default=0, help='toggle chat logging')
  parser.add_argument('-c', '--command', dest='!command', metavar=('cmd', 'args'), nargs='+', help='override server startup command (default is path to server executable)')
  parser.add_argument('-e', '--extra', dest='extra', metavar='options', nargs='+', help='additional options (order may change)')
  parser.add_argument('-f', '--filterscript', dest='filterscripts', metavar='path', action='append', help='load filter script (name or full/relative path); multiple occurences of this option are allowed')
  parser.add_argument('-g', '-g0', '--gamemode', '--gamemode0', dest='gamemode0', metavar='file', required=True, help='main game mode (name or full/relative path)')
  for i in range(1, 10):
    parser.add_argument('-g%d' % i, '--gamemode%d' % i, dest='gamemode%d' % i, metavar='file', help='game mode #%d' % i)
  parser.add_argument('-t', '--gamemodetext', dest='gamemodetext', metavar='"My Game Mode"', help='game mode text (shown in server browser)')
  parser.add_argument('-n', '--hostname', dest='hostname', metavar='"My SA-MP server"', help='host name (shown in server browser)')
  parser.add_argument('-l', '--lanmode', dest='lanmode', action='store_const', const=1, default=0, help='toggle LAN mode')
  parser.add_argument('--logqueries', action='store_const', const=1, default=0, help='toggle logging of queries sent by players')
  parser.add_argument('--logtimeformat', metavar='format', help='format of time stamps in log')
  parser.add_argument('-m', '--mapname', dest='mapname', metavar='name', help='map name (shown in server browser)')
  parser.add_argument('--maxplayers', metavar='number', type=int, default=500, help='max. number of players')
  parser.add_argument('--maxnpc', metavar='number', type=int, default=0, help='max. number of NPCs (bots)')
  parser.add_argument('-o', '--output', dest='output', action='store_const', const=1, default=0, help='toggle console output')
  parser.add_argument('-P', '--password', dest='password', metavar='password', nargs='?', const=generate_password(), help='server password')
  parser.add_argument('-s', '--serverdir', dest='!serverdir', metavar='path', help='server executable directory (current directory by default)')
  parser.add_argument('-d', '--plugin', dest='plugins', metavar='path', action='append', help='load plugin (name or full/relative path); multiple occurences of this option are allowed')
  parser.add_argument('-p', '--port', dest='port', metavar='number', type=int, default=7777, help='server port')
  parser.add_argument('-q', '--query', dest='query', action='store_const', const=1, default=0, help='allow querying server info from outside world (e.g. server browser)')
  parser.add_argument('-r', '--rcon', dest='rcon', action='store_const', const=1, default=0, help='toggle RCON (Remote CONsole)')
  parser.add_argument('-R', '--rconpassword', dest='rcon_password', metavar='password', default=generate_password(), help='RCON admin password')
  parser.add_argument('-T', '--timestamp', dest='timestamp', action='store_const', const=1, default=0, help='show time stamps in log')
  parser.add_argument('-u', '--weburl', dest='weburl', metavar='url', help='website URL')
  parser.add_argument('-w', '--workingdir', dest='!workingdir', metavar='path', default='.', help='set working directory (current directory by default)')

  args = parser.parse_args(sys.argv[1:])
  return vars(args)

def write_config(filename, options):
  file = open(filename, 'w')
  for name, value in options.items():
    if name.startswith('!'):
      continue
    if value is not None:
      file.write('%s %s\n' % (name, value))
  file.close()

def mkdir(path):
  if not os.path.exists(path):
    os.mkdir(path)

def group(n, iterable, padvalue=None):
    "group(3, 'abcdefg', 'x') --> ('a','b','c'), ('d','e','f'), ('g','x','x')"
    return itertools.izip_longest(*[iter(iterable)]*n, fillvalue=padvalue)

def run(options):
  working_dir = options['!workingdir']
  if not os.path.exists(working_dir):
    os.mkdir(working_dir)

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

  server_dir = options['!serverdir']
  if server_dir is None:
    server_dir = os.environ.get('SAMP_SERVER_ROOT')
    if server_dir is None:
      server_dir = os.getcwd()
  if not os.path.isabs(server_dir):
    server_dir = os.path.abspath(server_dir)

  command = options['!command']
  if command is None:
    if os.name == 'nt':
      server_exe = 'samp-server.exe'
    else:
      server_exe = 'samp03svr'
    command = os.path.join(server_dir, server_exe)

  extra = options['extra']
  if extra is not None:
    extra_options = dict(group(2, extra))
    options.update(extra_options)
    del options['extra']
  write_config(os.path.join(working_dir, 'server.cfg'), options)

  mkdir(os.path.join(working_dir, 'gamemodes'))
  mkdir(os.path.join(working_dir, 'filterscripts'))

  os.chdir(working_dir)
  try:
    subprocess.call(command)
  except KeyboardInterrupt:
    pass

if __name__ == '__main__':
  run(get_options())
