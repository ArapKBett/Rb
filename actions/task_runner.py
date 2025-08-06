from actions import roblox_client
import json

def run_all_tasks():
    with open('accounts/accounts.json') as f:
        accounts = json.load(f)

    for acc in accounts:
        cookie = acc["cookie"]
        roblox_client.join_game(cookie, GAME_UNIVERSE_ID)
        roblox_client.buy_egg(cookie, BUG_EGG_ITEM_ID)
        roblox_client.place_egg(cookie)
        roblox_client.leave_game(cookie)
      
