pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

def search_player_fbref(player_name):
    search_url = f"https://fbref.com/en/search/search.fcgi?search={player_name.replace(' ', '+')}"
    res = requests.get(search_url)
    soup = BeautifulSoup(res.text, 'html.parser')

    try:
        player_link = soup.select_one("div.search-item-url a")['href']
        full_url = "https://fbref.com" + player_link
        return full_url
    except Exception as e:
        print("Player not found.")
        return None

def get_goals_and_assists(player_url):
    res = requests.get(player_url)
    soup = BeautifulSoup(res.text, 'html.parser')

    try:
        stats_table = soup.find('table', {'id': 'stats_standard_dom_lg'})
        latest_season_row = stats_table.find_all('tbody')[0].find_all('tr')[-1]

        goals = latest_season_row.find('td', {'data-stat': 'goals'}).text
        assists = latest_season_row.find('td', {'data-stat': 'assists'}).text

        print(f"Goals: {goals}")
        print(f"Assists: {assists}")
    except Exception as e:
        print("Could not extract goals and assists.")

def get_player_stats(player_name):
    url = search_player_fbref(player_name)
    if url:
        get_goals_and_assists(url)

# Example
get_player_stats("Erling Haaland")
