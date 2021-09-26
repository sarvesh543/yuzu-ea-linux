import os
import sys
import requests


appDir = "~/.local/share/applications"
sourceLink = "https://github.com/pineappleEA/pineapple-src/releases/latest"
sourceDownloadLink = "https://github.com/pineappleEA/pineapple-src/releases/download/"


def findVersionNumber():
    ## returns 0 if the current version is not found
    os.chdir(os.path.expanduser(appDir))
    if os.path.exists(os.path.expanduser(f'{appDir}/yuzu-ea')) == False:
        os.mkdir('./yuzu-ea')

    dirList = os.listdir('./yuzu-ea')

    if len(dirList) > 1:
        os.rmdir('./yuzu-ea')
        os.mkdir('./yuzu-ea')
        return 0
    elif len(dirList) == 1:
        try:
            verNum = int(dirList[0][8:len(dirList[0]) - 9])
            return verNum
        except ValueError:
            os.rmdir('./yuzu-ea')
            os.mkdir('./yuzu-ea')
            return 0
    else:
        return 0


def checkIfNextVerExist(currVer): 
    ## returns 0 if current ver is the latest  
    response = requests.get(f'{sourceLink}')
    latestVerUrl = response.url
    nextVerStr = latestVerUrl[61:]
    nextVer = int(nextVerStr)
            
    if nextVer > currVer:       
        return nextVer    
    else:
        return 0


def updateAndReplace(currVer,nextVer):
    os.chdir(os.path.expanduser(f'{appDir}/yuzu-ea'))
    if currVer != 0:       
        os.remove(f'./Yuzu-EA-{currVer}.AppImage')
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
    os.chdir(os.path.expanduser(f'{appDir}/yuzu-ea'))
    os.system(f'./Yuzu-EA-{currVer}.AppImage')
    sys.exit(0)
else:
    os.system('echo "update available"')
    os.system('echo "Downloading update"')
    updateAndReplace(currVer,nextVer)


