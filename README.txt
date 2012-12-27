usage: samp-server-cli.py [-h] [-a] [-b address] [-C] [-c cmd [args ...]]
                          [-e name value [name value ...]] [-f name/path] -g
                          file [-g1 file] [-g2 file] [-g3 file] [-g4 file]
                          [-g5 file] [-g6 file] [-g7 file] [-g8 file]
                          [-g9 file] [-t "My Gamemode"] [-n "My SA-MP server"]
                          [-l] [--logqueries] [--logtimeformat format]
                          [-m name] [--maxplayers number] [--maxnpc number]
                          [-o] [-P [password]] [-s path] [-d name/path]
                          [-p number] [-q] [-r] [-R password] [-T] [-u url]
                          [-w path]

A command line interface to SA:MP server

optional arguments:
  -h, --help            show this help message and exit
  -a, --announce        announce to server masterlist
  -b address, --bind address
                        bind to specific IP address
  -C, --chatlogging     enable chat logging
  -c cmd [args ...], --command cmd [args ...]
                        override server startup command (path to server
                        executable by default)
  -e name value [name value ...], --extra name value [name value ...]
                        write additional options (order may change)
  -f name/path, --filterscript name/path
                        add filterscript; multiple occurences of this option
                        are allowed
  -g file, -g0 file, --gamemode file, --gamemode0 file
                        set startup game mode (mode #0)
  -g1 file, --gamemode1 file
                        set game mode #1
  -g2 file, --gamemode2 file
                        set game mode #2
  -g3 file, --gamemode3 file
                        set game mode #3
  -g4 file, --gamemode4 file
                        set game mode #4
  -g5 file, --gamemode5 file
                        set game mode #5
  -g6 file, --gamemode6 file
                        set game mode #6
  -g7 file, --gamemode7 file
                        set game mode #7
  -g8 file, --gamemode8 file
                        set game mode #8
  -g9 file, --gamemode9 file
                        set game mode #9
  -t "My Gamemode", --gamemodetext "My Gamemode"
                        set game mode text (shown in server browser)
  -n "My SA-MP server", --hostname "My SA-MP server"
                        set host name (shown in server browser)
  -l, --lanmode         enable LAN mode
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
  -s path, --serverdir path
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
  -w path, --workingdir path
                        set working directory (current directory by default)
