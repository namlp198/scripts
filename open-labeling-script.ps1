$path = Split-Path $MyInvocation.MyCommand.Path
$extend = "\\labelImg-master\\labelImg.py"
$path = $path + $extend
Start-Process python $path