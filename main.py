import subprocess
import threading
import time
import requests
from trackerConfiguration import *

processExited = False
servicePaused = False

def getAppList():
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
        print("servicePaused:", servicePaused)
        if servicePaused:
            time.sleep(10)
            continue

        appList = getAppList()

        if processExited:
            break

        ActiveApps = []
        for app in appList:
            for tracker in trackingData:
                if app == tracker["process"]:
                    ActiveApps.append(app)



        if not processExited and not servicePaused:
            fetchResult = requests.post(trackerURL, json={"secretCode": secretCode, "activeApps": ActiveApps})
        else:
            break

        if fetchResult.status_code != 200:
            print(f"Failed to push data to tracker, refetching in 20 seconds (CODE: {fetchResult.status_code})")
            for i in range(20):
                time.sleep(1)
                if processExited or servicePaused:
                    break
            if processExited:
                break
            if servicePaused:
                continue
            requests.post(trackerURL, json={"secretCode": secretCode, "activeApps": ActiveApps})

        for i in range(60):
            time.sleep(1)
            if processExited or servicePaused:
                break



def TRAY():
    import sys
    from pystray import Icon, MenuItem, Menu
    from PIL import Image, ImageDraw

    def create_image():
        image = Image.new("RGB", (64, 64), "black")
        draw = ImageDraw.Draw(image)
        draw.rectangle([16, 16, 48, 48], fill="white")
        return image

    def toggle_service(icon, item):
        global servicePaused
        servicePaused = not servicePaused
        icon.update_menu()

    def service_text(item):
        return "Run Service" if servicePaused else "Pause Service"

    def on_exit(icon):
        icon.stop()
        global processExited
        processExited = True
        sys.exit(0)

    def trayStart():
        menu = Menu(
            MenuItem("dsvl0.tracker", None, enabled=False),
            Menu.SEPARATOR,
            MenuItem(service_text, toggle_service),
            MenuItem("Stop Service", on_exit)
        )
        icon = Icon("test", create_image(), menu=menu)
        icon.run()

    trayStart()


if __name__ == "__main__":
    t = threading.Thread(target=TRAY, daemon=False)
    t.start()
    appTracker()