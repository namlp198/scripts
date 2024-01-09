$path = Split-Path $MyInvocation.MyCommand.Path
$folder_name = Split-Path $path -Leaf
$parent_path = Split-Path -Parent $path
$label_ext = "\\labels\\" + $folder_name
$path_copyto = $parent_path + $label_ext
$all_files_txt = $path + "\\*.txt"
Copy-Item -Path $all_files_txt -Destination $path_copyto