
This is a Python script that lets you easily run your server from the command
line without ever touching server.cfg. I personally use it all the time - it's
very convenient if you constantly change server settings, e.g. during testing.

Installation
------------

Use pip to install a stable version from Python package repository:

```sh
sudo pip intall samp-server-cli
```

or only for the current user:

```sh
pip install --user samp-server-cli
```

Alternatively, you can install samp-server-cli by running the accompanying
setup script:

```sh
python setup.py install
```

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
