import os
import requests
import time
import threading
import subprocess
from trackerConfiguration import *

def getAppList():
    # Get tasklist
    #tasklist = subprocess.check_output("tasklist", shell=False)

    tasklist = subprocess.run(["chcp", "1251", ">", "nul", "&&", "tasklist"], shell=True, capture_output=True, text=True)
    tasklist = tasklist.stdout
    appList = tasklist.split("\n")
    for i in range(len(appList)):
        if ".exe" in appList[i]:
            appList[i] = appList[i].split(".exe")[0] + ".exe"
        else:
            appList[i] = ""

    while "" in appList:
        appList.remove("")

    return appList


def appTracker():
    while True:
        appList = getAppList()


        ActiveApps = []
        for app in appList:
            for tracker in trackingData:
                if app == tracker["process"]:
                    ActiveApps.append(app)


        print("ActiveApps:", ActiveApps)
        fetchResult = requests.post(trackerURL, json={"secretCode": secretCode, "activeApps": ActiveApps})

        if fetchResult.status_code != 200:
            print(f"Failed to push data to tracker, refetching in 20 seconds (CODE: {fetchResult.status_code})")
            time.sleep(20)
            requests.post(trackerURL, json={"secretCode": secretCode, "activeApps": ActiveApps})

        time.sleep(60)



if __name__ == "__main__":
    appTracker()