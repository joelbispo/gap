# This script creates python files from ui.
# It needs to be run every time a ui files is changed.
# You need to execute it inside views folder


###### Activate conda environment
$env_name = "env_gap"
$conda_path = "C:\miniconda\envs\"
$env_path = $conda_path+$env_name

$conda_script = $env_path+"\Scripts"
$conda_lib = $env_path+"Library\bin"

$env:Path = "$conda_path;$conda_script;$conda_lib;$env:Path"

############################

$dir = ".\views\"
Get-Location

Get-ChildItem -Recurse $dir -Filter *.ui | 


Foreach-Object {
    $directory =  $_.DirectoryName+"\"
    $ui_file = $directory+$_
    #pyside2-uic mainwindow.ui > ui_mainwindow.py
    $new_python_file =$directory+ "ui_"+$_.Basename+".py"
    #pyside2-uic mainwindow.ui > ui_mainwindow.py
    pyside2-uic $ui_file -o $new_python_file
    echo "converted from: $ui_file to: $new_python_file"
}
echo "All uis converted"
exit 0

