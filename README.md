# yuzu-ea-linux

# About
* This script automatically updates yuzu to the
* latest ea version from [pineappleEA](https://github.com/pineappleEA/pineapple-src)
* and launches it

# Disclaimer
* Verify the script yourself before running
* There is no warranty of any kind

# Requirements
* Python 3
* requests module in python

# How to use
* Open terminal in directory containing the script
* Run the following command
* "python3 yuzuscript.py"

# Note
* If you wish to change the location where yuzu ea is stored
* then change value of 'appDir' in the script to
* "~/{whatever path or folder you want which exists}"

# Quick fixes
### Problem
* The script is showing
* "AppImage for latest yuzu early access does not exist in the release"
* and also does not launch Yuzu 
### Cause
* The latest release by [pineappleEA](https://github.com/pineappleEA/pineapple-src) does not contain appimage for linux
### Fix
* Go to [pineappleEA](https://github.com/pineappleEA/pineapple-src)
* and download the most recent yuzu ea appimage for linux from releases
* Now place the downloaded AppImage in '\~/.local/share/applications/yuzu-ea' or in '{appDir}/yuzu-ea' if you changed appDir in script and make it an excecutable
* before trying to run the script.
* The script should now launch yuzu normally and will update to the latest version as soon as it is available

       

