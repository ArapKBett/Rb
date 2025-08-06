import requests
import time

def is_bug_egg_available():
    # Simulated check; replace with real item ID or in-game API
    url = f"https://economy.roblox.com/v1/assets/{BUG_EGG_ITEM_ID}/resellers"
    response = requests.get(url)
    return response.status_code == 200 and response.json().get("data", [])

def monitor(callback):
    while True:
        if is_bug_egg_available():
            print("[+] Bug Egg is in stock!")
            callback()
            break
        else:
            print("[-] Still out of stock...")
        time.sleep(30)
              
