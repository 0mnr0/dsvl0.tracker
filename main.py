import os
import requests
import time
import threading
import subprocess
from trackerConfiguration import *

processExited = False

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
    while not processExited:
        appList = getAppList()

        if processExited:
            break

        ActiveApps = []
        for app in appList:
            for tracker in trackingData:
                if app == tracker["process"]:
                    ActiveApps.append(app)



        if not processExited:
            fetchResult = requests.post(trackerURL, json={"secretCode": secretCode, "activeApps": ActiveApps})
        else:
            break

        if fetchResult.status_code != 200:
            print(f"Failed to push data to tracker, refetching in 20 seconds (CODE: {fetchResult.status_code})")
            for i in range(20):
                time.sleep(1)
                if processExited:
                    break
            if processExited:
                break
            requests.post(trackerURL, json={"secretCode": secretCode, "activeApps": ActiveApps})

        for i in range(60):
            time.sleep(1)
            if processExited:
                break



def TRAY():
    import sys
    import threading
    from pystray import Icon, MenuItem, Menu
    from PIL import Image, ImageDraw

    def create_image():
        # Простая картинка (иконка) 16x16
        image = Image.new("RGB", (64, 64), "black")
        draw = ImageDraw.Draw(image)
        draw.rectangle([16, 16, 48, 48], fill="white")
        return image

    def on_exit(icon, item):
        icon.stop()
        global processExited
        processExited = True
        sys.exit(0)

    def trayStart():
        # Создаём меню
        menu = Menu(
            MenuItem("dsvl0.tracker", None, enabled=False),
            Menu.SEPARATOR,
            MenuItem("Выход", on_exit)
        )
        # Запускаем иконку
        icon = Icon("test", create_image(), menu=menu)
        icon.run()

    trayStart()


if __name__ == "__main__":
    t = threading.Thread(target=TRAY, daemon=False)
    t.start()
    appTracker()