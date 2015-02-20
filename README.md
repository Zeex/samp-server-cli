
This is a Python script that lets you easily run your server from the command
line without ever touching server.cfg. I personally use it all the time - it's
very convenient if you constantly change server settings, e.g. during testing.

Installation
------------

1. Install Python and it to PATH
2. Go to https://github.com/Zeex/samp-server-cli
3. Click "Download ZIP"
4. Extract samp-server-cli.py and batch/shell scripts somewhere:
   * Quick and easy: Extract to your server directory
   * Advanced: Extract anywhere and set the `SAMP_SERVER_ROOT` variable
5. Optional: Add samp-server-cli's directory to your PATH

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
