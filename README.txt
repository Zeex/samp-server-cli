usage: samp-server-cli.py [-h] [-a {0,1}] [-b address] [-chatlogging {0,1}]
                          [-f [path [path ...]]] -g path [-g1 path] [-g2 path]
                          [-g3 path] [-g4 path] [-g5 path] [-g6 path]
                          [-g7 path] [-g8 path] [-g9 path]
                          [-gamemodetext "My Game Mode"]
                          [-n "My SA-MP server"] [-l {0,1}]
                          [-logqueries {0,1}] [-logtimeformat format]
                          [-mapname name] [-maxplayers number]
                          [-maxnpc number] [-o {0,1}] [-password password]
                          [-s path] [-plugins [path [path ...]]] [-p number]
                          [-query {0,1}] [-rcon {0,1}]
                          [-rconpassword password] [-timestamp {0,1}]
                          [-weburl url] [-w path]

optional arguments:
  -h, --help            show this help message and exit
  -a {0,1}, -announce {0,1}
                        toggle announcement to masterlist
  -b address, -bind address
                        bind to specific IP address
  -chatlogging {0,1}    toggle chat logging
  -f [path [path ...]], -filterscripts [path [path ...]]
                        list of filter scripts to be loaded
  -g path, -g0 path, -gamemode path, -gamemode0 path
                        main game mode
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
  -gamemodetext "My Game Mode"
                        game mode text (shown in server browser)
  -n "My SA-MP server", -hostname "My SA-MP server"
                        host name (shown in server browser)
  -l {0,1}, -lanmode {0,1}
                        toggle LAN mode
  -logqueries {0,1}     toggle logging of queries sent by players
  -logtimeformat format
                        format of time stamps in log
  -mapname name         map name (shown in server browser)
  -maxplayers number    max. number of players
  -maxnpc number        max. number of NPCs (bots)
  -o {0,1}, -output {0,1}
                        toggle console output
  -password password    server password
  -s path, -serverdir path
                        server executable directory (current directory by
                        default)
  -plugins [path [path ...]]
                        list of plugins to be loaded
  -p number, -port number
                        server port
  -query {0,1}
  -rcon {0,1}           toggle RCON (Remote CONsole)
  -rconpassword password
                        RCON password
  -timestamp {0,1}      show time stamps in log
  -weburl url           website URL
  -w path, -workingdir path
                        set working directory (current directory by default)
