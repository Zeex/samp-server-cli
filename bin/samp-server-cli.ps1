$scriptPath = $MyInvocation.MyCommand.Definition
$scriptName = $MyInvocation.MyCommand.Name
$cliScriptPath = $scriptPath.Replace($scriptName, "") + "samp-server-cli.py"
python $cliScriptPath $args
