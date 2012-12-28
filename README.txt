usage: samp-server-cli.py [-h] [-a] [-b address] [--chatlogging]
                          [-c cmd [args ...]] [-C filename] [-D ...]
                          [-e name value [name value ...]] [-f name/path] -g
                          name/path [-g1 name/path] [-g2 name/path]
                          [-g3 name/path] [-g4 name/path] [-g5 name/path]
                          [-g6 name/path] [-g7 name/path] [-g8 name/path]
                          [-g9 name/path] [-t "My Game Mode"]
                          [-n "My SA-MP server"] [-l] [-L] [--logqueries]
                          [--logtimeformat format] [-m name]
                          [--maxplayers number] [--maxnpc number] [-o]
                          [-P [password]] [-s path] [-d name/path] [-p number]
                          [-q] [-r] [-R password] [-T] [-u url] [-w path]

A command line interface to SA:MP server

optional arguments:
  -h, --help            show this help message and exit
  -a, --announce        announce to server masterlist
  -b address, --bind address
                        bind to specific IP address
  --chatlogging         enable chat logging
  -c cmd [args ...], --command cmd [args ...]
                        override server startup command (path to server
                        executable by default)
  -C filename, --config filename
                        copy options from file
  -D ..., --debug ...   run under debugger
  -e name value [name value ...], --extra name value [name value ...]
                        write additional options (order may change)
  -f name/path, --filterscript name/path
                        add filter script; multiple occurences of this option
                        are allowed
  -g name/path, -g0 name/path, --gamemode name/path, --gamemode0 name/path
                        set startup game mode (mode #0)
  -g1 name/path, --gamemode1 name/path
                        set game mode #1
  -g2 name/path, --gamemode2 name/path
                        set game mode #2
  -g3 name/path, --gamemode3 name/path
                        set game mode #3
  -g4 name/path, --gamemode4 name/path
                        set game mode #4
  -g5 name/path, --gamemode5 name/path
                        set game mode #5
  -g6 name/path, --gamemode6 name/path
                        set game mode #6
  -g7 name/path, --gamemode7 name/path
                        set game mode #7
  -g8 name/path, --gamemode8 name/path
                        set game mode #8
  -g9 name/path, --gamemode9 name/path
                        set game mode #9
  -t "My Game Mode", --gamemodetext "My Game Mode"
                        set game mode text (shown in server browser)
  -n "My SA-MP server", --hostname "My SA-MP server"
                        set host name (shown in server browser)
  -l, --lanmode         enable LAN mode
  -L, --local           run in current directory (same as if you pass "--
                        workdir .")
  --logqueries          enable logging of queries sent by players
  --logtimeformat format
                        set log timestamp format
  -m name, --mapname name
                        set map name (shown in server browser)
  --maxplayers number   set max. number of players
  --maxnpc number       set max. number of NPCs (bots)
  -o, --output          enable console output
  -P [password], --password [password]
                        server password
  -s path, --servdir path
                        set directory of server executable (current directory
                        by default); not necesssary if you use -c
  -d name/path, --plugin name/path
                        add plugin; multiple occurences of this option are
                        allowed
  -p number, --port number
                        set server port
  -q, --query           allow querying server info from outside world (e.g.
                        server browser)
  -r, --rcon            enable RCON (Remote CONsole) access
  -R password, --rconpassword password
                        RCON admin password
  -T, --timestamp       show timestamps in log
  -u url, --weburl url  website URL
  -w path, --workdir path
                        set working directory (server directory by default)
