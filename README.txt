usage: samp-server-cli [-h] [-a] [-b address] [--chatlogging]
                       [-c cmd [args ...]] [-D ...] [-e filename]
                       [-E name value [name value ...]] [-f name/path] -g
                       name/path [-g1 name/path] [-g2 name/path]
                       [-g3 name/path] [-g4 name/path] [-g5 name/path]
                       [-g6 name/path] [-g7 name/path] [-g8 name/path]
                       [-g9 name/path] [--gamemodetext "My Game Mode"]
                       [-n "My SA-MP server"] [--incar-rate ms] [-l] [-L] [-Q]
                       [--logtimeformat format] [-m name] [--maxnpc number]
                       [--maxplayers number] [--myriad] [--nosign]
                       [--onfoot-rate ms] [-o] [-P [password]] [-d name/path]
                       [-p number] [-q] [-r] [-R password] [-s path]
                       [--sleep ms] [--stream-distance float]
                       [--stream-rate ms] [-t] [-T sec] [--weapon-rate ms]
                       [-u url] [-w path]

A command line interface to SA:MP server

optional arguments:
  -h, --help            show this help message and exit
  -a, --announce        announce to server masterlist
  -b address, --bind address
                        bind to specific IP address
  --chatlogging         enable logging of in-game chat
  -c cmd [args ...], --command cmd [args ...]
                        override server startup command (path to server
                        executable by default)
  -D ..., --debug ...   run server under debugger
  -e filename, --exec filename
                        load options from file
  -E name value [name value ...], --extra name value [name value ...]
                        additional server.cfg options (order may change)
  -f name/path, --filterscript name/path
                        add a filter script; multiple occurences of this
                        option are allowed
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
  --gamemodetext "My Game Mode"
                        set game mode text (shown in server browser)
  -n "My SA-MP server", --hostname "My SA-MP server"
                        set host name (shown in server browser)
  --incar-rate ms       set player data update rate while in a vehicle
  -l, --lanmode         enable LAN mode
  -L, --local           run in current directory (same as if you pass "--
                        workdir .")
  -Q, --logqueries      enable logging of queries sent to the server
  --logtimeformat format
                        set log timestamp format
  -m name, --mapname name
                        set map name (shown in server browser)
  --maxnpc number       set max. number of NPCs (bots)
  --maxplayers number   set max. number of players
  --myriad              ??
  --nosign              ??
  --onfoot-rate ms      set player data update rate while walking/running
  -o, --output          enable console output (Linux only)
  -P [password], --password [password]
                        set server password
  -d name/path, --plugin name/path
                        add a plugin; multiple occurences of this option are
                        allowed
  -p number, --port number
                        set server listen port
  -q, --query           allow querying server info from outside world (e.g.
                        server browser)
  -r, --rcon            enable RCON (Remote CONsole)
  -R password, --rcon-password password
                        set RCON password
  -s path, --servdir path
                        set server's root directory (current directory by
                        default); not necesssary if you use -c
  --sleep ms            set server sleep time
  --stream-distance float
                        set stream distance
  --stream-rate ms      set stream rate
  -t, --timestamp       enable timestamps in log
  -T sec, --timeout sec
                        limit server run time
  --weapon-rate ms      set player data update rate while firing a weapon
  -u url, --weburl url  set contact website URL
  -w path, --workdir path
                        set working directory (server directory by default)
