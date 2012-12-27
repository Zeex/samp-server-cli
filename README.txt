usage: samp-server-cli.py [-h] [-a] [-b address] [-C] [-c cmd [args ...]]
                          [-e options [options ...]] [-f file1 [file2 ...]] -g
                          file [-g1 file] [-g2 file] [-g3 file] [-g4 file]
                          [-g5 file] [-g6 file] [-g7 file] [-g8 file]
                          [-g9 file] [-t "My Game Mode"]
                          [-n "My SA-MP server"] [-l] [-logqueries]
                          [-logtimeformat format] [-m name]
                          [-maxplayers number] [-maxnpc number] [-o]
                          [-P [password]] [-s path]
                          [-plugins file1 [file2 ...]] [-p number] [-q] [-r]
                          [-R password] [-T] [-u url] [-w path]

optional arguments:
  -h, --help            show this help message and exit
  -a, -announce         toggle announcement to masterlist
  -b address, -bind address
                        bind to specific IP address
  -C, -chatlogging      toggle chat logging
  -c cmd [args ...], -command cmd [args ...]
                        override server startup command (default is path to
                        server executable)
  -e options [options ...], -extra options [options ...]
                        additional options (order may change)
  -f file1 [file2 ...], -filterscripts file1 [file2 ...]
                        list of filter scripts to be loaded (full or relative
                        paths or just @names
  -g file, -g0 file, -gamemode file, -gamemode0 file
                        main game mode (full or relative path or just @name)
  -g1 file, -gamemode1 file
                        game mode #1
  -g2 file, -gamemode2 file
                        game mode #2
  -g3 file, -gamemode3 file
                        game mode #3
  -g4 file, -gamemode4 file
                        game mode #4
  -g5 file, -gamemode5 file
                        game mode #5
  -g6 file, -gamemode6 file
                        game mode #6
  -g7 file, -gamemode7 file
                        game mode #7
  -g8 file, -gamemode8 file
                        game mode #8
  -g9 file, -gamemode9 file
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
  -plugins file1 [file2 ...]
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
