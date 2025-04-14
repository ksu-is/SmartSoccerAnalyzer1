pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

def search_sofascore_player(player_name):
    search_url = f"https://www.sofascore.com/search?q={player_name.replace(' ', '%20')}"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    res = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    try:
        player_path = soup.select_one('a[href^="/player/"]')['href']
        return "https://www.sofascore.com" + player_path
    except:
        return None

def get_sofascore_stats(player_url):
    res = requests.get(player_url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(res.text, 'html.parser')

    print(f"\n📊 Stats for: {player_url}")

    try:
        player_name = soup.select_one("h1").text.strip()
        print(f"\nPlayer: {player_name}")

        profile_items = soup.select(".sc-ecffda1b-0.eUvcrH p")
        if profile_items:
            print("Position:", profile_items[0].text)
            print("Team:", profile_items[1].text)

        stat_blocks = soup.select(".sc-aef7b5d7-0.kDObUw .sc-ecffda1b-0")
        print("\n📈 Season Stats:")
        for block in stat_blocks:
            label = block.select_one("p.sc-ecffda1b-3").text
            value = block.select_one("p.sc-ecffda1b-1").text
            print(f"{label}: {value}")
    except Exception as e:
        print("⚠️ Could not parse stats.")

def get_player_stats(player_name):
    url = search_sofascore_player(player_name)
    if url:
        get_sofascore_stats(url)
    else:
        print("Player not found.")

player = input("Enter player name: ")
get_player_stats(player)
