#!/usr/bin/env python
#
# Copyright (c) 2012-2019 Zeex
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
import shutil
import string
import subprocess
import sys
import threading

try:
  from itertools import izip_longest
except ImportError:
  from itertools import zip_longest as izip_longest

SERVER_CFG_OPTIONS = [
  'announce',
  'bind',
  'chatlogging',
  'debug',
  'filterscripts',
  'gamemode0',
  'gamemode1',
  'gamemode2',
  'gamemode3',
  'gamemode4',
  'gamemode5',
  'gamemode6',
  'gamemode7',
  'gamemode8',
  'gamemode9',
  'gamemodetext',
  'hostname',
  'incar_rate',
  'lagcompmode',
  'lanmode',
  'logqueries',
  'logtimeformat',
  'mapname',
  'maxnpc',
  'maxplayers',
  'myriad',
  'nosign',
  'onfoot_rate',
  'output',
  'password',
  'plugins',
  'port',
  'query',
  'rcon',
  'rcon_password',
  'sleep',
  'stream_distance',
  'stream_rate',
  'timestamp',
  'weapon_rate',
  'weburl',
]

class Timer:
  def __init__(self, timeout, callback):
    self.callback = callback
    self.timer = threading.Timer(timeout, self.on_timeout)
    self.is_expired = False

  def start(self):
    self.timer.start()

  def cancel(self):
    self.timer.cancel()

  def on_timeout(self):
    self.is_expired = True
    self.callback()

class Server:
  def __init__(self, optons):
    self.set_options(optons)

  def is_valid_config_option(self, name):
    if name in SERVER_CFG_OPTIONS:
      return True
    extra_options = self.options.get('extra_options')
    if extra_options is not None:
      for o in extra_options:
        if name == o[0]:
          return True
    return False

  def read_config(self, filename):
    self.options = {}
    with open(filename, 'r') as file:
      for line in file.readlines():
        try:
          name, value = string.split(line.strip(), maxsplit=1)
          self.options[name] = value
        except ValueError:
          name = line.strip()
          if len(name) > 0:
            self.options[name] = ''

  def write_config(self, filename):
    with open(filename, 'w') as file:
      cfg_optons = {
        k:v for (k, v) in self.options.items()
          if self.is_valid_config_option(k)
      }
      for name, value in cfg_optons.items():
        if value is not None:
          if len(str(value)) > 0:
            file.write('%s %s\n' % (name, value))
          else:
            file.write('%s\n' % name)

  def get_server_dir(self):
    servdir = self.options.get('servdir')
    if servdir is None:
      servdir = os.environ.get('SAMP_SERVER_ROOT')
      if servdir is None:
        servdir = os.getcwd()
    if not os.path.isabs(servdir):
      servdir = os.path.abspath(servdir)
    return servdir

  def get_working_dir(self):
    local = self.options.get('local')
    if local:
      workdir = os.getcwd()
    else:
      workdir = self.options.get('workdir')
      if workdir is None:
        workdir = self.get_server_dir()
    return workdir

  def get_server_command(self):
    command = self.options.get('command')
    if command is None:
      exe = os.environ.get('SAMP_SERVER')
      if not exe:
        if os.name == 'nt':
          exe = 'samp-server.exe'
        else:
          exe = 'samp03svr'
      exe_paths = [
        os.path.join(self.get_server_dir(), exe),
        os.path.join(os.path.dirname(os.path.realpath(__file__)), exe)
      ]
      for path in exe_paths:
        if os.path.exists(path):
          command = [path]
          break
    return command

  def get_command(self):
    debug = self.options.get('debug')
    if debug is None:
      return self.get_server_command()
    if os.name == 'nt':
      return ['ollydbg'] + debug + self.get_server_command()
    else:
      return ['gdb'] + debug + ['--args'] + self.get_server_command()

  def set_options(self, options):
    self.options = dict(options)

    extra_options = self.options.get('extra_options')
    if extra_options is not None:
      for o in extra_options:
        head, tail = o[0], o[1:]
        self.options[head] = ' '.join(tail)

    rcon_password = self.options.get('rcon_password')
    if rcon_password is not None:
      self.options['rcon'] = 1
    else:
      self.options['rcon_password'] = generate_password()

    plugins = self.options.get('plugins')
    if plugins is not None:
      if os.name == 'nt':
        plugin_extension = '.dll'
      else:
        plugin_extension = '.so'
      for i, p in enumerate(plugins):
        if not p.lower().endswith(plugin_extension):
          plugins[i] += plugin_extension

    dirs = { 'filterscripts': 'filterscripts',
             'plugins':       'plugins',
           }
    for i in range(0, 10):
      dirs['gamemode%d' % i] = 'gamemodes'

    for name, dir in dirs.items():
      dir = os.path.join(self.get_working_dir(), dir)
      values = self.options[name]
      if values is None:
        continue
      if type(values) is not list:
        values = [values]
      if values is not None:
        for i, v in enumerate(values):
          values[i] = convert_path(v, dir)
        self.options[name] = '%s' % ' '.join(values)

  def run(self):
    if self.options.get('no_launch'):
      return 0

    command = self.get_command()
    workdir = self.get_working_dir()

    if command is None:
      raise Exception('Could not find SA-MP server')

    for dir in ['', 'filterscripts', 'gamemodes', 'plugins']:
      real_dir = os.path.join(workdir, dir)
      if not os.path.exists(real_dir):
        os.mkdir(real_dir)

    if not self.options.get('no_config'):
      config = self.options.get('config')
      if config is None:
        server_cfg = os.path.join(workdir, 'server.cfg')
        self.write_config(server_cfg)
      else:
        config_paths = [
          os.path.join(workdir, 'configs', config),
          os.path.join(workdir, 'configs', config + '.cfg'),
          os.path.join(workdir, convert_path(config, workdir)),
          os.path.join(workdir, convert_path(config, workdir) + '.cfg'),
        ]
        config_path = None
        for path in config_paths:
          if os.path.exists(path):
            config_path = path
            shutil.copy(path, os.path.join(workdir, 'server.cfg'))
            break
        if config_path is None:
          raise Exception(
            'Could not find the config file. '
            'Tried the follwoing paths:\n- %s' % '\n- '.join(config_paths))

    os.chdir(workdir)
    process = subprocess.Popen(command)

    timeout = self.options.get('timeout')
    if not timeout:
      process.wait()
    else:
      timeout_timer = Timer(timeout, process.terminate)
      timeout_timer.start()
      process.wait()
      if timeout_timer.is_expired:
        return 1
      else:
        timeout_timer.cancel()
    return process.returncode

def generate_password(size=10,
                      chars=string.ascii_letters + string.digits):
  return ''.join(random.choice(chars) for x in range(size))

def convert_path(path, dir):
  if os.path.isabs(path) or path.startswith('.'):
    return os.path.relpath(os.path.realpath(path), dir)
  return path

def parse_options(args):
  parser = argparse.ArgumentParser(
    description='A command line interface to SA:MP server',
    fromfile_prefix_chars='@')

  parser.add_argument('-a', '--announce', dest='announce',
    action='store_const', const=1, default=0,
    help='announce to server masterlist')

  parser.add_argument('-b', '--bind', dest='bind',
    metavar='address',
    help='bind to specific IP address')

  parser.add_argument('--chatlogging', dest='chatlogging',
    action='store_const', const=1, default=0,
    help='enable logging of in-game chat')

  parser.add_argument('-c', '--command', dest='command',
    nargs='+', metavar=('cmd', 'args'),
    help='override server startup command (path to server executable '
         'by default)')

  parser.add_argument('-C', '--config', dest='config',
    metavar='filename',
    help='use existing server.cfg file')

  parser.add_argument('-D', '--debug', dest='debug',
    nargs=argparse.REMAINDER,
    help='run server under debugger')

  parser.add_argument('-f', '--filterscript', dest='filterscripts',
    metavar='name/path', action='append',
    help='add a filter script; multiple occurences of this option are allowed')

  parser.add_argument('-g', '-g0', '--gamemode', '--gamemode0', dest='gamemode0',
    metavar='name/path', default='bare',
    help='set startup game mode (mode #0)')

  for i in range(1, 10):
    parser.add_argument('-g%d' % i, '--gamemode%d' % i, dest='gamemode%d' % i,
      metavar='name/path',
      help='set game mode #%d' % i)

  parser.add_argument('--gamemodetext', dest='gamemodetext',
    metavar='"My Game Mode"',
    help='set game mode text (shown in server browser)')

  parser.add_argument('-n', '--hostname', dest='hostname',
    metavar='"My SA-MP server"',
    help='set host name (shown in server browser)')

  parser.add_argument('--incar-rate', dest='incar_rate',
    metavar='ms',
    help='set player data update rate while in a vehicle')

  parser.add_argument('--lagcompmode', dest='lagcompmode',
    metavar='mode', type=int, choices=[0, 1, 2], default=0,
    help='set lag compensation mode')

  parser.add_argument('-l', '--lanmode', dest='lanmode',
    action='store_const', const=1, default=0,
    help='enable LAN mode')

  parser.add_argument('-L', '--local', dest='local',
    action='store_true', default=False,
    help='run in current directory (same as if you pass "--workdir .")')

  parser.add_argument('-Q', '--logqueries', dest='logqueries',
    action='store_const', const=1, default=0,
    help='enable logging of queries sent to the server')

  parser.add_argument('--logtimeformat', dest='logtimeformat',
    metavar='format',
    help='set log timestamp format')

  parser.add_argument('-m', '--mapname', dest='mapname',
    metavar='name',
    help='set map name (shown in server browser)')

  parser.add_argument('-N', '--maxnpc', dest='maxnpc',
    metavar='number', type=int, default=0,
    help='set max. number of NPCs (bots)')

  parser.add_argument('-M', '--maxplayers', dest='maxplayers',
    metavar='number', type=int, default=500,
    help='set max. number of players')

  parser.add_argument('--myriad', dest='myriad',
    action='store_const', const=1, default=0,
    help='??')

  parser.add_argument('--nosign', dest='nosign',
    action='store_const', const=1, default=0,
    help='??')

  parser.add_argument('--no-launch', dest='no_launch',
    action='store_true', default=False,
    help='don\'t start the server, just write server.cfg')

  parser.add_argument('--no-config', dest='no_config',
    action='store_true', default=False,
    help='don\'t write server.cfg, just start the server')

  parser.add_argument('--onfoot-rate', dest='onfoot_rate',
    metavar='ms',
    help='set player data update rate while walking/running')

  parser.add_argument('-o', '--output', dest='output',
    action='store_const', const=1, default=0,
    help='enable console output (Linux only)')

  parser.add_argument('-P', '--password', dest='password',
    nargs='?', metavar='password', const=generate_password(),
    help='set server password')

  parser.add_argument('-d', '--plugin', dest='plugins',
    metavar='name/path', action='append',
    help='add a plugin; multiple occurences of this option are allowed')

  parser.add_argument('-p', '--port', dest='port',
    metavar='number', type=int, default=7777,
    help='set server listen port')

  parser.add_argument('-q', '--query', dest='query',
    action='store_const', const=1, default=0,
    help='allow querying server info from outside world (e.g. server browser)')

  parser.add_argument('-r', '--rcon', dest='rcon',
    action='store_const', const=1, default=0,
    help='enable RCON (Remote CONsole)')

  parser.add_argument('-R', '--rcon-password', dest='rcon_password',
    metavar='password',
    help='set RCON password (implies --rcon)')

  parser.add_argument('-s', '--servdir', dest='servdir',
    metavar='path',
    help='set server\'s root directory (current directory by default); '
         'not necesssary if you use -c')

  parser.add_argument('--sleep', dest='sleep',
    metavar='ms',
    help='set server sleep time')

  parser.add_argument('--stream-distance', dest='stream_distance',
    metavar='float',
    help='set stream distance')

  parser.add_argument('--stream-rate', dest='stream_rate',
      metavar='ms',
      help='set stream rate')

  parser.add_argument('-t', '--timestamp', dest='timestamp',
    action='store_const', const=1, default=0,
    help='enable timestamps in log')

  parser.add_argument('-T', '--timeout', dest='timeout',
    metavar='sec', type=float,
    help='shut down after X seconds')

  parser.add_argument('--weapon-rate', dest='weapon_rate',
    metavar='ms',
    help='set player data update rate while firing a weapon')

  parser.add_argument('-u', '--weburl', dest='weburl',
    metavar='url',
    help='set contact website URL')

  parser.add_argument('-w', '--workdir', dest='workdir',
    metavar='path',
    help='set working directory (server directory by default)')

  parser.add_argument('-x', dest='extra_options',
    nargs='+', metavar=('name', 'value'), action='append',
    help='add a custom server.cfg setting; '
         'multiple occurences of this option are allowed')

  return vars(parser.parse_args(args))

def main():
  try:
    server = Server(parse_options(sys.argv[1:]))
    return server.run()
  except KeyboardInterrupt:
    pass

if __name__ == '__main__':
  sys.exit(main())
