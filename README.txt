usage: samp-server-cli.py [-h] [-a] [-b address] [-C]
                          [-e [options [options ...]]] [-f [path [path ...]]]
                          -g path [-g1 path] [-g2 path] [-g3 path] [-g4 path]
                          [-g5 path] [-g6 path] [-g7 path] [-g8 path]
                          [-g9 path] [-t "My Game Mode"]
                          [-n "My SA-MP server"] [-l] [-logqueries]
                          [-logtimeformat format] [-m name]
                          [-maxplayers number] [-maxnpc number] [-o]
                          [-P [password]] [-s path]
                          [-plugins [path [path ...]]] [-p number] [-q] [-r]
                          [-R password] [-T] [-u url] [-w path]

optional arguments:
  -h, --help            show this help message and exit
  -a, -announce         toggle announcement to masterlist
  -b address, -bind address
                        bind to specific IP address
  -C, -chatlogging      toggle chat logging
  -e [options [options ...]], -extra [options [options ...]]
                        additional options (order may change)
  -f [path [path ...]], -filterscripts [path [path ...]]
                        list of filter scripts to be loaded (full or relative
                        paths or just @names
  -g path, -g0 path, -gamemode path, -gamemode0 path
                        main game mode (full or relative path or just @name)
  -g1 path, -gamemode1 path
                        game mode #1
  -g2 path, -gamemode2 path
                        game mode #2
  -g3 path, -gamemode3 path
                        game mode #3
  -g4 path, -gamemode4 path
                        game mode #4
  -g5 path, -gamemode5 path
                        game mode #5
  -g6 path, -gamemode6 path
                        game mode #6
  -g7 path, -gamemode7 path
                        game mode #7
  -g8 path, -gamemode8 path
                        game mode #8
  -g9 path, -gamemode9 path
                        game mode #9
  -t "My Game Mode", -gamemodetext "My Game Mode"
                        game mode text (shown in server browser)
  -n "My SA-MP server", -hostname "My SA-MP server"
                        host name (shown in server browser)
  -l, -lanmode          toggle LAN mode
  -logqueries           toggle logging of queries sent by players
  -logtimeformat format
                        format of time stamps in log
  -m name, -mapname name
                        map name (shown in server browser)
  -maxplayers number    max. number of players
  -maxnpc number        max. number of NPCs (bots)
  -o, -output           toggle console output
  -P [password], -password [password]
                        server password
  -s path, -serverdir path
                        server executable directory (current directory by
                        default)
  -plugins [path [path ...]]
                        list of plugins to be loaded (full or relative paths
                        or just @names)
  -p number, -port number
                        server port
  -q, -query            allow querying server info from outside world (e.g.
                        server browser)
  -r, -rcon             toggle RCON (Remote CONsole)
  -R password, -rconpassword password
                        RCON admin password
  -T, -timestamp        show time stamps in log
  -u url, -weburl url   website URL
  -w path, -workingdir path
                        set working directory (current directory by default)
