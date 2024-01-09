$path = Split-Path $MyInvocation.MyCommand.Path
$extend = "\\remove_img_no_labeling.py"
$path_0 = $path + $extend
Start-Process python $path_0