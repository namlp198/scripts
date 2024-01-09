$path = Split-Path $MyInvocation.MyCommand.Path
# $path = "E:\\ml\\yl\\src\\darknet_train"
$txt_1 = "\\cmd_train_text.txt"
$txt_2 = "\\cmd_trainv4_text.txt"
$filePath = $path + $txt_2
$cmd = Get-Content -Path $filePath
# $cmd = "./darknet detect cfg/yolov3.cfg yolov3.weights data/person.jpg"
Start-Process powershell $cmd