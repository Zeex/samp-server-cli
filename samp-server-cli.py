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
import os
import random
import string
import subprocess
import sys

def generate_password(size=10, chars=string.ascii_letters + string.digits):
  return ''.join(random.choice(chars) for x in range(size))

def get_options():
  parser = argparse.ArgumentParser()

  parser.add_argument('-a', '-announce', dest='announce', action='store_const', const=1, default=0, help='toggle announcement to masterlist')
  parser.add_argument('-b', '-bind', dest='bind', metavar='address', help='bind to specific IP address')
  parser.add_argument('-c', '-chatlogging', dest='chatlogging', action='store_const', const=1, default=0, help='toggle chat logging')
  parser.add_argument('-f', '-filterscripts', dest='filterscripts', metavar='path', nargs='*', help='list of filter scripts to be loaded (full or relative paths or just @names')
  parser.add_argument('-g', '-g0', '-gamemode', '-gamemode0', dest='gamemode0', metavar='path', required=True, help='main game mode (full or relative path or just @name)')
  for i in range(1, 10):
    parser.add_argument('-g%d' % i, '-gamemode%d' % i, dest='gamemode%d' % i, metavar='path', help='game mode #%d' % i)
  parser.add_argument('-x', '-gamemodetext', dest='gamemodetext', metavar='"My Game Mode"', help='game mode text (shown in server browser)')
  parser.add_argument('-n', '-hostname', dest='hostname', metavar='"My SA-MP server"', help='host name (shown in server browser)')
  parser.add_argument('-l', '-lanmode', dest='lanmode', action='store_const', const=1, default=0, help='toggle LAN mode')
  parser.add_argument('-logqueries', action='store_const', const=1, default=0, help='toggle logging of queries sent by players')
  parser.add_argument('-logtimeformat', metavar='format', help='format of time stamps in log')
  parser.add_argument('-m', '-mapname', dest='mapname', metavar='name', help='map name (shown in server browser)')
  parser.add_argument('-maxplayers', metavar='number', type=int, default=500, help='max. number of players')
  parser.add_argument('-maxnpc', metavar='number', type=int, default=0, help='max. number of NPCs (bots)')
  parser.add_argument('-o', '-output', dest='output', action='store_const', const=1, default=0, help='toggle console output')
  parser.add_argument('-P', '-password', dest='password', metavar='password', help='server password')
  parser.add_argument('-s', '-serverdir', dest='!serverdir', metavar='path', default='', help='server executable directory (current directory by default)')
  parser.add_argument('-plugins', metavar='path', nargs='*', help='list of plugins to be loaded (full or relative paths or just @names)')
  parser.add_argument('-p', '-port', dest='port', metavar='number', type=int, default=7777, help='server port')
  parser.add_argument('-q', '-query', dest='query', action='store_const', const=1, default=0)
  parser.add_argument('-r', '-rcon', dest='rcon', action='store_const', const=1, default=0, help='toggle RCON (Remote CONsole)')
  parser.add_argument('-R', '-rconpassword', dest='rcon_password', metavar='password', default=generate_password(), help='RCON admin password')
  parser.add_argument('-t', '-timestamp', dest='timestamp', action='store_const', const=1, default=0, help='show time stamps in log')
  parser.add_argument('-u', '-weburl', dest='weburl', metavar='url', help='website URL')
  parser.add_argument('-w', '-workingdir', dest='!workingdir', metavar='path', default='.', help='set working directory (current directory by default)')

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
        if v.startswith('@'):
          values[i] = v[1:]
        else:
          values[i] = os.path.relpath(v, dir)
      options[name] = '%s' % ' '.join(values)

  server_dir = os.path.abspath(options['!serverdir'])
  if os.name == 'nt':
    server_exe = 'samp-server.exe'
  else:
    server_exe = 'samp03svr'
  server_path = os.path.join(server_dir, server_exe)

  write_config(os.path.join(working_dir, 'server.cfg'), options)

  mkdir(os.path.join(working_dir, 'gamemodes'))
  mkdir(os.path.join(working_dir, 'filterscripts'))

  os.chdir(working_dir)
  subprocess.call(server_path)

if __name__ == '__main__':
  run(get_options())
