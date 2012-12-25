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
  -announce {0,1}       Toggle announcement
  -bind address         Bind to specific IP address
  -filterscripts [path [path ...]]
                        List of filter scripts to be loaded
  -gamemode0 path       Main game mode
  -gamemode1 path       Game mode #1
  -gamemode2 path       Game mode #2
  -gamemode3 path       Game mode #3
  -gamemode4 path       Game mode #4
  -gamemode5 path       Game mode #5
  -gamemode6 path       Game mode #6
  -gamemode7 path       Game mode #7
  -gamemode8 path       Game mode #8
  -gamemode9 path       Game mode #9
  -gamemodetext "My Game Mode"
                        Game mode text (shown in server browser)
  -hostname "My SA-MP server"
                        Host name (shown in server browser)
  -lanmode {0,1}        Toggle LAN mode
  -logtimeformat format
                        Format of time stamps in log
  -mapname name         Map name (shown in server browser)
  -maxplayers number    Max. number of players
  -maxnpc number        Max. number of NPCs (bots)
  -output {0,1}         Toggle console output
  -password password    Server password
  -serverdir path       Path to server root
  -plugins [path [path ...]]
                        List of plugins to be loaded
  -port number          Server port
  -query {0,1}
  -rcon {0,1}           Toggle RCON (Remote CONsole)
  -rcon_password password
                        RCON password
  -timestamp {0,1}      Show time stamps in log
  -weburl url           Website URL
  -workingdir path      Working directory
