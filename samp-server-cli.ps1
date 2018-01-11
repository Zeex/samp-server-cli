$scriptPath = $MyInvocation.MyCommand.Definition
$scriptName = $MyInvocation.MyCommand.Name
$cliScriptPath = $scriptPath.Replace($scriptName, "") + "samp_server_cli.py"
python $cliScriptPath $args
