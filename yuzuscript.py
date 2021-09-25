import os
import sys
import requests


appDir = "~/.local/share/applications"
sourceLink = "https://github.com/pineappleEA/pineapple-src/releases/latest"
sourceDownloadLink = "https://github.com/pineappleEA/pineapple-src/releases/download/"


def findVersionNumber():
    os.chdir(os.path.expanduser(appDir))
    if os.path.exists(os.path.expanduser(f'{appDir}/yuzu')) == False:
        os.mkdir('./yuzu')

    dirList = os.listdir('./yuzu')

    if len(dirList) > 1:
        os.rmdir('./yuzu')
        os.mkdir('./yuzu')
        return 0
    elif len(dirList) == 1:
        verNumStr = dirList[0][8:len(dirList[0]) - 9]
        return int(verNumStr)
    else:
        return 0


def checkIfNextVerExist(currVer):    
    response = requests.get(f'{sourceLink}')
    latestVerUrl = response.url
    nextVerStr = latestVerUrl[61:]
    nextVer = int(nextVerStr)
            
    if nextVer > currVer:       
        return nextVer    
    else:
        return 0


def updateAndReplace(currVer,nextVer):
    os.chdir(os.path.expanduser(appDir))
    if currVer != 0:
        os.chdir(os.path.expanduser(appDir))        
        os.remove(f'./yuzu/Yuzu-EA-{currVer}.AppImage')
    os.chdir(os.path.expanduser(f'{appDir}/yuzu'))
    os.system(f'wget "{sourceDownloadLink}EA-{nextVer}/Yuzu-EA-{nextVer}.AppImage"')
    os.system('echo "download complete"')
    os.system(f'chmod +x Yuzu-EA-{nextVer}.AppImage')
    os.system('echo "Launching Yuzu"')
    os.system(f'./Yuzu-EA-{nextVer}.AppImage')
    sys.exit(0)


## checking and updating
os.system('echo "checking for updates..."')
currVer = findVersionNumber()
nextVer = checkIfNextVerExist(currVer)

if nextVer == 0:
    os.system('echo "Already on latest version"')
    os.system('echo "Launching Yuzu"')
    os.chdir(os.path.expanduser(f'{appDir}/yuzu'))
    os.system(f'./Yuzu-EA-{currVer}.AppImage')
    sys.exit(0)
else:
    os.system('echo "update available"')
    os.system('echo "Downloading update"')
    updateAndReplace(currVer,nextVer)


