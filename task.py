import subprocess
import json
import os
def wifiPassRetrieve():
    data = subprocess.check_output(['netsh','wlan','show', 'profiles']).decode('utf-8').split('\n')[9:-2]
    wifiNamesList = []
    wifiNamePassDict = {}
    for x in range(len(data)):
        userProfileName = data[x].split(':')[1].strip('\r').lstrip(" ")
        wifiNamesList.append(str(userProfileName))
    for name in wifiNamesList:
        commandName = " ".join(['netsh','wlan','show','profile','name=','"'+str(name)+'"', "key=clear"])
        passWordDetail = subprocess.check_output(commandName).decode('utf-8').split('\n')[-12].split(":")[1].lstrip(" ").strip("\r")
        wifiNamePassDict[name] = str(passWordDetail)
    file = open(os.path.abspath("WifiPasswords.json"),'w')
    json.dump(wifiNamePassDict, file)
    print(wifiNamePassDict)

if __name__ == "__main__":
    objWifi= wifiPassRetrieve()
