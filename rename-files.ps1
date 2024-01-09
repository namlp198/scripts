$path = Split-Path $MyInvocation.MyCommand.Path
$classes_file = "\\classes.txt"
$dst = "\\data\\data_new"
$path_dst = $path + $dst
$path_classes_file_0 = $path_dst + $classes_file
$path_classes_file_1 = $path + $classes_file
Remove-Item -Path $path_classes_file_0
$extend = "\\rename_files.py"
$path_0 = $path + $extend
Start-Process python $path_0
Start-Sleep -Seconds 1
read-host “Press ENTER to end...”
Copy-Item -Path $path_classes_file_1 -Destination $path_dst


#read-host “Press ENTER to continue...”

#$arr_ext = "\\data\\data_new\\*.png","\\data\\data_new\\*.jpg","\\data\\data_new\\*.jpeg","\\data\\data_new\\*.tif"
#foreach($ele in $arr_ext){
#	$path_ext_0 = $path + $ele
#	Remove-Item -Path $path_ext_0
#}
#$arr_rename_ext = "\\data\\img_renamed\\*.png","\\data\\img_renamed\\*.jpg","\\data\\img_renamed\\*.jpeg","\\data\\img_renamed\\*.tif"
#$data_new = "\\data\\data_new\\"
#$path_des = $path + $data_new
#foreach($ele in $arr_rename_ext){
#	$path_ext_1 = $path + $ele
#	Move-Item -Path $path_ext_1 -Destination $path_des
#}