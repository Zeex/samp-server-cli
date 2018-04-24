
This is a shell script that lets you quickly start your SA-MP server from
the command line without opening, editing, and saving `server.cfg` every
time. It's usually useful during development.

How to use it
-------------

You can define the root directory by setting `SAMP_SERVER_ROOT` (see below)
and run the server from anywhere. If you're working on a plugin and want to
test it, you just do:

```
samp-server-cli -d ./path/to/plugin.so
```

By default `samp-server-cli` uses the "bare" gamemode (`gamemodes/bare.pwn`).
If you want to test some code snippet that you compiled to `somescript.amx`
simply run:

```
samp-server-cli -g ./somescript
```

(the `.amx` part should be omitted)

When you use `./` in front of a file name passed to `-d`, `-g`, or `-f` it
means that it's relative to the current working directory. When you don't,
it means that the path is relative to the corresponding directory (`plugins`,
`gamemodes`, and `filterscripts` respectively).

Installation
------------

Use pip to install a stable version from the Python Package Index:

```sh
sudo pip install samp-server-cli
```

or only for the current user:

```sh
pip install --user samp-server-cli
```

This will create a shell script in your `~/.local/bin` or `/usr/local/bin`
directory on Linux and a .exe file in `C:\PythonXY\Scripts` on Windows.

Alternatively, you can install samp-server-cli by running the accompanying
setup script:

```sh
python setup.py install
```

Finally, you can just download this repository and run samp-server-cli out
of the box using one of the wrapper scripts shipped with the source code.

Post-install configuration
--------------------------

One thing you may need to do after installing samp-server-cli is to set
the `SAMP_SERVER_ROOT` environment variable to the absolute path to your
server's root directory (where samp03svr or samp-server.exe sits). This
is only needed if you install samp-server-cli in some non-default location.

By default, server executables are searched in:

* The current working directory
* The directory in which samp-server-cli is located
* The value of the `SAM_SERVER_ROOT` variable

You can also specify the exact command to be run instead using `--coomand`,
in which case the script will not attempt to find the server executable.

Examples
--------

Running a gamemode with default settings:

```
samp-server-cli -g grandlarc
```

Running a publicly accessible server with maxplayers 10 and RCON
password "test":

```
samp-server-cli -g grandlarc -q -R test -M 10
```

Using filterscripts:

```
samp-server-cli -g grandlarc -f fsdebug -f gl_actions -f gl_realtime
```

Using plugins:

```
samp-server-cli -g grandlarc -d crashdetect -d streamer
```

Adding non-standard server.cfg options:

```
samp-server-cli -g grandlarc -d profiler -x some_option its_value
```

Using existing server.cfg file:

```
samp-server-cli --no-config
```

Reading command line arguments from a file:

```
samp-server-cli @filename
```

Other options
-------------

To see the complete list of command line options run `samp-server-cli -h`.
