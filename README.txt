usage: samp-server-cli.py [-h] [-announce {0,1}] [-bind address]
                          [-filterscripts [path [path ...]]] -gamemode0 path
                          [-gamemode1 path] [-gamemode2 path]
                          [-gamemode3 path] [-gamemode4 path]
                          [-gamemode5 path] [-gamemode6 path]
                          [-gamemode7 path] [-gamemode8 path]
                          [-gamemode9 path] [-gamemodetext "My Game Mode"]
                          [-hostname "My SA-MP server"] [-lanmode {0,1}]
                          [-logtimeformat format] [-mapname name]
                          [-maxplayers number] [-maxnpc number]
                          [-output {0,1}] [-password password]
                          [-serverdir path] [-plugins [path [path ...]]]
                          [-port number] [-query {0,1}] [-rcon {0,1}]
                          [-rcon_password password] [-timestamp {0,1}]
                          [-weburl url] [-workingdir path]

optional arguments:
  -h, --help            show this help message and exit
  -announce {0,1}       toggle announcement to masterlist
  -bind address         bind to specific IP address
  -filterscripts [path [path ...]]
                        list of filter scripts to be loaded
  -gamemode0 path       main game mode
  -gamemode1 path       game mode #1
  -gamemode2 path       game mode #2
  -gamemode3 path       game mode #3
  -gamemode4 path       game mode #4
  -gamemode5 path       game mode #5
  -gamemode6 path       game mode #6
  -gamemode7 path       game mode #7
  -gamemode8 path       game mode #8
  -gamemode9 path       game mode #9
  -gamemodetext "My Game Mode"
                        game mode text (shown in server browser)
  -hostname "My SA-MP server"
                        host name (shown in server browser)
  -lanmode {0,1}        toggle LAN mode
  -logtimeformat format
                        format of time stamps in log
  -mapname name         map name (shown in server browser)
  -maxplayers number    max. number of players
  -maxnpc number        max. number of NPCs (bots)
  -output {0,1}         toggle console output
  -password password    server password
  -serverdir path       server executable directory (current directory by
                        default)
  -plugins [path [path ...]]
                        list of plugins to be loaded
  -port number          server port
  -query {0,1}
  -rcon {0,1}           toggle RCON (Remote CONsole)
  -rcon_password password
                        RCON password
  -timestamp {0,1}      show time stamps in log
  -weburl url           website URL
  -workingdir path      set working directory (current directory by default)
