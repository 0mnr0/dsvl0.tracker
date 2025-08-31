trackerURL = "https://dsvl0.space/devTracker/push"

secretCode = None
try:
    secretCode = open('secret.key', 'r').read()
except:
    try:
        secretCode = open('dsvl0_tracker/secret.key', 'r').read()
    except:
        raise Exception("Secret key not found (secret.key)")

trackerPushURL = "/devTracker/push"

trackingData = [
    {
        "process": "PEAK.exe",
        "isGame": True,
        "displayName": "PEAK",
    }, {
        "process": "7DaysToDie.exe",
        "isGame": True,
        "displayName": "7 Days To Die",
    }, {
        "process": "Phasmophobia.exe",
        "isGame": True,
        "displayName": "Phasmophobia",
    }, {
        "process": "FSD.exe",
        "isGame": True,
        "displayName": "Deep Rock Galactic",
    },
    {
        "process": "Minecraft.exe",
        "isGame": True,
        "displayName": "Minecraft",
    },
    {
        "process": "UltimateChickenHorse.exe",
        "isGame": True,
        "displayName": "Ultimate Chicken Horse",
    }
]