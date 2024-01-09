$path = Split-Path $MyInvocation.MyCommand.Path
$arr_ext = "\\data\\data_new\\*.png","\\data\\data_new\\*.jpg","\\data\\data_new\\*.jpeg","\\data\\data_new\\*.tif","\\data\\data_new\\*.txt"
$data_train = "\\data\\data_train"
$path_des = $path + $data_train
foreach($ele in $arr_ext){
	$path_ext = $path + $ele
	Move-Item -Path $path_ext -Destination $path_des
}
$classes = "\\data\\data_train\\classes.txt"
$new = "\\data\\data_new"
$path_classes = $path + $classes
$path_new = $path + $new
Move-Item -Path $path_classes  -Destination $path_new
read-host “Press ENTER to continue...”
$extend = "\\create_train_valid_auto.py"
$path_0 = $path + $extend
Start-Process python $path_0

